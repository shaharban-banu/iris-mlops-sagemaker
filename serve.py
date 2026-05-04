import subprocess
import sys

# SageMaker will call: docker run image serve
# So we ignore "serve" and start FastAPI

if __name__ == "__main__":
    subprocess.run([
        "uvicorn",
        "app:app",
        "--host", "0.0.0.0",
        "--port", "8080"
    ])