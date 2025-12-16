# ---- Base Image ----
FROM python:3.10-slim-bullseye

# ---- Set working directory ----
WORKDIR /app

# ---- Install system dependencies ----
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
        gnupg2 \
        ca-certificates \
        lsb-release \
        sudo \
        wget \
    && rm -rf /var/lib/apt/lists/*

# ---- Install Node.js 20 LTS ----
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy app files ----
COPY . /app

# ---- Upgrade pip and install Python dependencies ----
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# ---- Set environment variables for Railway ----
# Railway will automatically inject ENV variables like API_ID, API_HASH, TOKEN, etc.
# Make sure you add these in Railway Dashboard: Settings → Variables

# ---- Run the bot ----
CMD ["python", "main.py"]
