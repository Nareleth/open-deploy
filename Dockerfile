FROM debian:bookworm-slim

WORKDIR /app

COPY . .

RUN apt update && apt install -y \
    python3 \
    python3-flask

EXPOSE 8080
CMD ["python3", "/app/server/server.py"]