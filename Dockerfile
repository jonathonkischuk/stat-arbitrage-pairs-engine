FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y python3-tk libtk8.6 libx11-6 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
