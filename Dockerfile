# Base image: Python 3.9 on Debian Bullseye
FROM python:3.9-slim-bullseye

# Avoid interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies, Node.js 20 LTS, and clean apt cache
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        ffmpeg \
        build-essential \
        gnupg2 \
        ca-certificates \
        python3-pip \
        apt-transport-https \
        lsb-release \
        sudo && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
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
