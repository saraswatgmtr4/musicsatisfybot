# Base image: Python 3.9 on Debian Bullseye
FROM python:3.10-slim

# Avoid interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies, Node.js 20 LTS, and clean apt cache
# Install system dependencies
RUN apt-get update && apt-get install -y \
        git \
        curl \
        ffmpeg \
        build-essential \
        python3-dev \
        libffi-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
        libjpeg-dev \
        libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /app/requirements.txt


# Upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python3", "main.py"]




