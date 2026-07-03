# Dockerfile Best Practices — Annotated Examples

## The reference multi-stage build (Node.js, same ideas apply everywhere)

```dockerfile
# ---- Stage 1: build (heavy toolchain, never shipped) ----
FROM node:22.12-alpine AS build          # pin minor version, never :latest
WORKDIR /app

# Copy manifests FIRST so the dependency layer caches until deps change
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts               # ci (not install): reproducible, lockfile-strict

COPY . .
RUN npm run build && npm prune --omit=dev # drop devDependencies from the tree

# ---- Stage 2: runtime (minimal, non-root) ----
FROM node:22.12-alpine AS runtime
ENV NODE_ENV=production
WORKDIR /app

# Non-root user: containers escaping as uid 0 are a real attack class
RUN addgroup -S app && adduser -S app -G app
USER app

COPY --from=build --chown=app:app /app/node_modules ./node_modules
COPY --from=build --chown=app:app /app/dist ./dist

EXPOSE 3000
# Exec form so the process receives SIGTERM directly (graceful shutdown works)
CMD ["node", "dist/server.js"]
```

Result: ~120 MB instead of ~1.1 GB single-stage, no compilers or npm cache in prod.

## Layer-ordering rule

Order instructions from least- to most-frequently changing:

1. Base image
2. System packages (`apk add` / `apt-get install` in ONE RUN with cleanup)
3. Dependency manifests + install
4. Application source
5. Build step

One line of app code changed = only layers 4–5 rebuild.

## Anti-patterns and their fixes

| Anti-pattern | Why it hurts | Fix |
|---|---|---|
| `FROM node:latest` | Unreproducible builds; surprise breakage | Pin `node:22.12-alpine`, ideally by digest in prod |
| `COPY . .` before install | Any file change busts the dependency cache | Copy manifests first, source later |
| `RUN apt-get update` alone in its own layer | Stale package index cached forever | `apt-get update && apt-get install -y --no-install-recommends X && rm -rf /var/lib/apt/lists/*` in one RUN |
| Running as root (default) | Container escape = host root pivot | `USER app` after creating an unprivileged user |
| Secrets via `ARG`/`ENV` or `COPY .env` | Baked into image history forever | BuildKit `RUN --mount=type=secret,id=token ...` |
| `CMD npm start` (shell form via npm) | npm swallows SIGTERM; pods take 30s+ to die | Exec form calling node directly |
| No `.dockerignore` | `.git`, `node_modules`, secrets sent to daemon | Ignore `.git`, `node_modules`, `*.env`, coverage, docs |
| `ADD` for local files | Surprising tar/URL magic | Use `COPY`; reserve `ADD` for verified remote archives |

## Hardening checklist

- [ ] Distroless (`gcr.io/distroless/*`) or alpine base; final image < 200 MB
- [ ] `USER` is non-root; `readOnlyRootFilesystem: true` in the pod spec
- [ ] HEALTHCHECK defined (or rely on K8s probes — don't duplicate both)
- [ ] Image scanned in CI (Trivy: `trivy image --severity CRITICAL,HIGH --exit-code 1`)
- [ ] Labels for traceability: `org.opencontainers.image.revision=$GIT_SHA`
- [ ] Deployed by digest (`image@sha256:...`), tags treated as human-friendly aliases only
