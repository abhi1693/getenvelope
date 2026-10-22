# GetEnvelope

A project and service email inbox with agent assistance, planned for self-hosted and hosted use.

This repository currently contains the application scaffold: a FastAPI backend, a Next.js frontend,
development tooling, and container packaging. Email, providers, authentication, tenancy, persistence,
and agent workflows have not been implemented.

## 0.0.1

Refresh backend and frontend dependencies, including the Node.js 26 type definitions, while keeping
the existing scaffold behavior and locked installation workflow.

## Layout

```text
backend/     FastAPI application using the Python src layout
frontend/    Next.js App Router application
docs/        Local research and planning; ignored by Git
```

The workspace follows DevFeed's uv/npm conventions with one backend and one frontend.

## Requirements

- Python 3.12 and [uv](https://docs.astral.sh/uv/)
- Node.js 22.22.2+ on 22.x, 24.15.0+ on 24.x, or 26+
- npm
- Docker Compose for the optional container setup

## Local development

Install dependencies from the repository root:

```sh
uv sync --all-packages --locked
npm ci
```

Start each application in a separate terminal:

```sh
npm run backend:dev
```

```sh
npm run frontend:dev
```

The frontend runs at <http://localhost:3000>. The API health endpoint is
<http://127.0.0.1:8000/health>, and its OpenAPI interface is at <http://127.0.0.1:8000/docs>.

## Checks and builds

```sh
npm run check
npm run frontend:build
```

Run `npm run format` to format Python and frontend files. Python dependencies are locked in `uv.lock`;
JavaScript dependencies are locked in `package-lock.json`.

The workspace reuses DevFeed's MIT-licensed, depth-limited braces implementation for the unpatched
[upstream advisory](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm). Its parser and AST walkers reject
excessive nesting; `npm run check` includes the malicious-input and ordinary-glob regression tests.
The frontend image copies this local package before the locked install. No advisory is suppressed;
replace the fork when an audited upstream fix is available. See [the package security notes](packages/braces/SECURITY.md).

## Containers

```sh
docker compose up --build
```

Both services bind to localhost. This runs only the scaffold; it does not provision mail providers,
databases, authentication, or production infrastructure.

## Local research

Research is available locally at `docs/README.md` and `docs/mvp-research.md`. The entire `/docs/`
directory is ignored by Git and excluded from Docker build contexts. It will not appear in a fresh
clone. Do not force-add these files.
