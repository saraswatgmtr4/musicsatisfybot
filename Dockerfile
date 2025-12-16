# Use Python 3.9 on a supported Debian base
FROM python:3.9-slim-bullseye

# Set environment variables to avoid prompts during installs
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies, Node.js, and clean up apt cache
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        ffmpeg \
        build-essential \
        python3-pip && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Default command
CMD ["python3", "main.py"]
