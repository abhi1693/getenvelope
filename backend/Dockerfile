FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
COPY backend/pyproject.toml backend/pyproject.toml
RUN uv sync --locked --no-dev --no-install-workspace --package getenvelope-backend

COPY backend/src backend/src
RUN uv sync --locked --no-dev --no-editable --package getenvelope-backend

FROM python:3.12-slim-bookworm AS runner

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN groupadd --system --gid 10001 app \
    && useradd --system --uid 10001 --gid app app

COPY --from=builder --chown=app:app /app/.venv /app/.venv
USER app

EXPOSE 8000
CMD ["uvicorn", "getenvelope_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--no-proxy-headers"]
