FROM python:3.10-slim

WORKDIR /workspace

COPY workspace/requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    nano \
    vim \
    tzdata && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

ENV TZ=Asia/Tokyo
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    echo "Asia/Tokyo" > /etc/timezone
