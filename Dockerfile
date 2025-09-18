FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY *.py ./
COPY README.md ./

# Create directory for credentials and output
RUN mkdir -p /app/data

# Set environment variables to use data directory
ENV GOOGLE_CREDENTIALS_FILE=/app/data/credentials.json
ENV GOOGLE_TOKEN_FILE=/app/data/token.json

VOLUME ["/app/data"]

# Make main.py executable
RUN chmod +x main.py

ENTRYPOINT ["python", "main.py"]