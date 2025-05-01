from flask import Flask
import redis
import os

app = Flask(__name__)

# Read Redis host/port from environment
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def home():
    return "Welcome to my DevOps app!"

@app.route("/visit")
def visit():
    try:
        count = r.incr("counter")
        return f"Visit count: {count}"
    except redis.exceptions.ConnectionError:
        return "Cannot connect to Redis", 500

@app.route("/health")
def health():
    try:
        r.ping()
        return "Healthy", 200
    except redis.exceptions.ConnectionError:
        return "Unhealthy", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
