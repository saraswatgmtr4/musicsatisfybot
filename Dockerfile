# Use official Python slim image
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# --------------------------
# 1️⃣ Install system dependencies
# --------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    gnupg2 \
    lsb-release \
    curl \
    sudo \
    git \
    ffmpeg \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# --------------------------
# 2️⃣ Install Node.js 20 LTS
# --------------------------
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm \
    && rm -rf /var/lib/apt/lists/*

# --------------------------
# 3️⃣ Upgrade pip & install Python packages
# --------------------------
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# --------------------------
# 4️⃣ Copy the bot source code
# --------------------------
COPY . /app

# --------------------------
# 5️⃣ Set environment variables defaults (Railway will override)
# --------------------------
ENV API_ID=123456
ENV API_HASH="your_api_hash"
ENV BOT_TOKEN="your_bot_token"
ENV SESSION_STRING="your_session_string"

# --------------------------
# 6️⃣ Run the bot
# --------------------------
CMD ["python", "main.py"]
