# =========================
# Stage 1: Build stage
# =========================
FROM python:3.13-slim AS builder

WORKDIR /src/rest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# Copy requirements first for caching
COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# =========================
# Stage 2: Production / Dev stage
# =========================
FROM python:3.13-slim

RUN useradd -m -r appuser && \
    mkdir -p /app && \
    chown -R appuser /app

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy application code
COPY --chown=appuser:appuser src/rest/ .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ENV_TYPE=development

USER appuser

EXPOSE 8000

# Use Django dev server for now
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
