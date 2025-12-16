# Use Python 3.9 on Debian Bullseye
FROM python:3.9-slim-bullseye

# Avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and Node.js prerequisites
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        curl \
        ffmpeg \
        build-essential \
        gnupg2 \
        ca-certificates \
        python3-pip \
        wget \
        dirmngr \
        lsb-release \
        sudo && \
    rm -rf /var/lib/apt/lists/*

# Install Node.js 16.x
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
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
