# Playwright Patterns for Stable, Fast E2E Suites

## 1. Locator strategy — in strict priority order

```typescript
// 1. Role-based (accessible, survives refactors, enforces a11y)
page.getByRole('button', { name: 'Submit order' })
// 2. Label / placeholder for form fields
page.getByLabel('Email address')
// 3. Test IDs — only when role/label genuinely can't work
page.getByTestId('cart-line-item')
// NEVER: CSS chains or XPath tied to DOM structure
// BAD: page.locator('div.container > ul li:nth-child(3) span')
```

## 2. No manual waits — trust web-first assertions

```typescript
// BAD: race conditions and wasted seconds
await page.waitForTimeout(3000);

// GOOD: auto-retrying assertion, resolves as soon as true (default 5s timeout)
await expect(page.getByRole('alert')).toHaveText('Order confirmed');

// GOOD: wait for the API response that drives the UI, then assert
const responsePromise = page.waitForResponse(r =>
  r.url().includes('/api/orders') && r.status() === 201);
await page.getByRole('button', { name: 'Place order' }).click();
await responsePromise;
```

## 3. Authenticate once, reuse everywhere (saves ~5s per test)

```typescript
// global.setup.ts — runs once, saves session to disk
await page.goto('/login');
await page.getByLabel('Email').fill(process.env.TEST_USER!);
await page.getByLabel('Password').fill(process.env.TEST_PASS!);
await page.getByRole('button', { name: 'Sign in' }).click();
await expect(page.getByRole('navigation')).toBeVisible(); // confirm before saving!
await page.context().storageState({ path: '.auth/user.json' });

// playwright.config.ts
use: { storageState: '.auth/user.json' }
```

## 4. Seed data via API, verify via UI

```typescript
// Creating test data through the UI makes every test slow and coupled.
test('user can cancel an order', async ({ page, request }) => {
  // Arrange: fast, deterministic API seeding
  const order = await request.post('/api/test/orders', {
    data: { sku: 'WIDGET-1', qty: 2 },
  }).then(r => r.json());

  // Act + Assert: only the behavior under test goes through the UI
  await page.goto(`/orders/${order.id}`);
  await page.getByRole('button', { name: 'Cancel order' }).click();
  await expect(page.getByText('Cancelled')).toBeVisible();
});
```

## 5. Page Object Model — thin, action-oriented

```typescript
export class CheckoutPage {
  constructor(private page: Page) {}
  readonly payButton = () => this.page.getByRole('button', { name: 'Pay now' });

  async payWithCard(card: TestCard) {
    await this.page.getByLabel('Card number').fill(card.number);
    await this.payButton().click();
  }
  // Assertions live in tests, not page objects — keeps failures readable.
}
```

## 6. Config that fights flakiness for you

```typescript
export default defineConfig({
  retries: process.env.CI ? 1 : 0,     // 1 retry in CI; a test needing 2 is broken
  fullyParallel: true,                  // forces test isolation discipline
  forbidOnly: !!process.env.CI,         // no accidental .only in CI
  use: {
    trace: 'on-first-retry',            // full trace for every flaky occurrence
    video: 'retain-on-failure',
  },
});
```

Rule of thumb: if a test passes on retry, treat it as FAILED for trust purposes —
log it, track its pass rate, and fix the root cause within a sprint.
