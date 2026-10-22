# Build from the repository root: docker build -f frontend/Dockerfile .
FROM node:24-alpine AS builder
WORKDIR /app
ENV NEXT_TELEMETRY_DISABLED=1
COPY package.json package-lock.json ./
COPY packages/braces packages/braces
COPY frontend/package.json frontend/package.json
RUN --mount=type=cache,target=/root/.npm npm ci --no-audit --no-fund
COPY frontend frontend
RUN --mount=type=cache,target=/app/frontend/.next/cache,sharing=locked \
    npm run build --workspace @getenvelope/frontend

FROM node:24-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 HOSTNAME=0.0.0.0 PORT=3000
COPY --from=builder --chown=node:node /app/frontend/.next/standalone ./
COPY --from=builder --chown=node:node /app/frontend/.next/static ./frontend/.next/static
COPY --from=builder --chown=node:node /app/frontend/public ./frontend/public
USER node
EXPOSE 3000
CMD ["node", "frontend/server.js"]
