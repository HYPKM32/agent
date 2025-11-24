FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# 시스템 패키지 설치 (screen 추가)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    screen \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
RUN pip install --upgrade pip && \
    pip install google-adk && \
    pip install asyncio-atexit && \
    pip install fastapi && \
    pip install uvicorn && \
    pip install websockets && \
    pip install litellm

# 포트 노출
EXPOSE 8894

# 기본 명령어
CMD ["/bin/bash"]