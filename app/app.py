from flask import Flask, jsonify
from config import Config
from logger import logger

app = Flask(__name__)

@app.route("/")
def home():
    logger.info("Root endpoint accessed")
    return jsonify({
        "message": "Welcome to CloudCart Product Service"
    })

@app.route("/health")
def health():
    logger.info("Health check endpoint accessed")
    return jsonify({
        "status": "healthy",
        "service": Config.APP_NAME
    })

if __name__ == "__main__":
    logger.info(f"Starting {Config.APP_NAME} in {Config.ENV} mode on port {Config.PORT}")
    app.run(host="0.0.0.0", port=Config.PORT)

