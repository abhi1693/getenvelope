FROM ghcr.io/astral-sh/uv:0.13.5@sha256:32a7bb39b496babbd997b0a39a4d66c126bdaf5661b302bf6f06abda8deca6ff AS uv

FROM python:3.12.15-slim-bookworm@sha256:6a0e06f5ba0b373d051aabd3fffb9b873f27f9a2a3a14bcbe37dee6f0e3bbc70 AS python-base

FROM python-base AS builder
COPY --from=uv /uv /usr/local/bin/uv

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
COPY backend/pyproject.toml backend/pyproject.toml
RUN uv sync --locked --no-dev --no-install-workspace --package getenvelope-backend

COPY backend/src backend/src
RUN uv sync --locked --no-dev --no-editable --package getenvelope-backend

FROM python-base AS runner

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN groupadd --system --gid 10001 app \
    && useradd --system --uid 10001 --gid app app

COPY --from=builder --chown=app:app /app/.venv /app/.venv
USER app
RUN python -c 'import os, ssl, uvloop; from getenvelope_api.main import app; assert os.getuid() == 10001; assert app.openapi()["paths"]; assert ssl.create_default_context().get_ca_certs()'

EXPOSE 8000
CMD ["uvicorn", "getenvelope_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--no-proxy-headers"]
