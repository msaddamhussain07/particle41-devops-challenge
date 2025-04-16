FROM python:3.13-alpine

# Creating a non-root user
RUN adduser -D appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

WORKDIR /app

# Copy requierments first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COpy app files
COPY --chown==appuser:appuser . .

# Switch to non-root user
USER appuser

# Expose port and run the app
EXPOSE 5000
CMD [ "python", "main.py"]