import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = int(os.getenv("PORT", 5000))
    ENV = os.getenv("ENV", "development")
    APP_NAME = os.getenv("APP_NAME", "cloudcart-product-service")

