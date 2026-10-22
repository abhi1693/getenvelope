# Build from the repository root: docker build -f frontend/Dockerfile .
FROM node:26.12.1-alpine3.24@sha256:40cd011b55415bc894e45b02fdd5a5dfde056921b7d23a64c74f80497af48797 AS builder
WORKDIR /app
ENV NEXT_TELEMETRY_DISABLED=1
COPY package.json package-lock.json ./
COPY packages/braces packages/braces
COPY frontend/package.json frontend/package.json
RUN --mount=type=cache,target=/root/.npm npm ci --no-audit --no-fund
COPY frontend frontend
RUN --mount=type=cache,target=/app/frontend/.next/cache,sharing=locked \
    npm run build --workspace @getenvelope/frontend

FROM node:26.12.1-alpine3.24@sha256:40cd011b55415bc894e45b02fdd5a5dfde056921b7d23a64c74f80497af48797 AS runtime
WORKDIR /app
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 HOSTNAME=0.0.0.0 PORT=3000
COPY --from=builder --chown=node:node /app/frontend/.next/standalone ./
COPY --from=builder --chown=node:node /app/frontend/.next/static ./frontend/.next/static
COPY --from=builder --chown=node:node /app/frontend/public ./frontend/public
USER node
RUN node --version && node -e 'require("next/package.json")'
EXPOSE 3000
CMD ["node", "frontend/server.js"]
