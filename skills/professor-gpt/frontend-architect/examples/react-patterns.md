# Canonical React Patterns

Reference implementations for the component API rules in SKILL.md.

## 1. Compound Components (composition over configuration)

```tsx
// ❌ Configuration soup — every new need adds a prop
<Card title="Billing" icon={<Gear/>} footerAction={save} collapsible />

// ✅ Composition — consumers arrange the parts
const CardContext = createContext<{ id: string } | null>(null);

export function Card({ children }: { children: ReactNode }) {
  const id = useId();
  return (
    <CardContext.Provider value={{ id }}>
      <section aria-labelledby={id} className="card">{children}</section>
    </CardContext.Provider>
  );
}
Card.Header = function CardHeader({ children }: { children: ReactNode }) {
  const ctx = useContext(CardContext)!;
  return <h3 id={ctx.id} className="card-header">{children}</h3>;
};
Card.Body = ({ children }: { children: ReactNode }) => (
  <div className="card-body">{children}</div>
);
```

## 2. Controlled AND Uncontrolled (like native inputs)

```tsx
function useControllableState<T>(opts: {
  value?: T; defaultValue: T; onChange?: (v: T) => void;
}) {
  const [internal, setInternal] = useState(opts.defaultValue);
  const isControlled = opts.value !== undefined;
  const value = isControlled ? (opts.value as T) : internal;
  const setValue = useCallback((next: T) => {
    if (!isControlled) setInternal(next);
    opts.onChange?.(next);
  }, [isControlled, opts.onChange]);
  return [value, setValue] as const;
}

// <Accordion defaultOpen /> just works; <Accordion open={o} onOpenChange={setO} /> too.
```

## 3. Server State Belongs in a Query Cache

```tsx
// ❌ Hand-rolled fetch state: no cache, no dedupe, race conditions
useEffect(() => { fetch(url).then(r => r.json()).then(setData); }, [url]);

// ✅ TanStack Query: caching, dedupe, retries, invalidation
const { data, isPending, error } = useQuery({
  queryKey: ["orders", { page, status }],
  queryFn: () => fetchOrders({ page, status }),
  staleTime: 30_000,           // deliberate freshness decision
  placeholderData: keepPreviousData,  // no layout flash on page change
});
```

## 4. URL as State (shareable, refresh-proof)

```tsx
// Filters, tabs, pagination → search params, not useState
const [status, setStatus] = useQueryState("status",
  parseAsStringLiteral(["open", "closed"] as const).withDefault("open"));
// Back button, deep links, and "share this view" all work for free.
```

## 5. Keeping Interactions Under the 200 ms INP Budget

```tsx
const [query, setQuery] = useState("");
const [isPending, startTransition] = useTransition();

function onSearch(e: ChangeEvent<HTMLInputElement>) {
  setQuery(e.target.value);                    // urgent: keep input responsive
  startTransition(() => setFilter(e.target.value)); // non-urgent: heavy list
}
// Plus: virtualize the result list (>100 rows) with @tanstack/react-virtual.
```

## 6. Typed Variants, Not Boolean Soup

```tsx
const button = cva("btn", {
  variants: {
    variant: { primary: "btn-primary", destructive: "btn-destructive" },
    size: { sm: "h-8 px-3 text-sm", md: "h-10 px-4" },
  },
  defaultVariants: { variant: "primary", size: "md" },
});

type ButtonProps = ComponentPropsWithoutRef<"button"> & VariantProps<typeof button>;

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  function Button({ variant, size, className, ...rest }, ref) {
    return <button ref={ref}
      className={cn(button({ variant, size }), className)} // consumer wins last
      {...rest} />;                                          // rest spread LAST
  }
);
```

## Anti-Pattern Quick List

- `useEffect` syncing one piece of state into another → derive it during render.
- API data copied into Redux/Zustand → query cache owns server state.
- Context providing a fast-changing value app-wide → split contexts or use a store with selectors.
- `React.memo` everywhere "for performance" → profile first; fix the re-render source.
