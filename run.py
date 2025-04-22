from app import create_app
import os

app = create_app(os.getenv("APP_CONFIG", "app.config.DevelopmentConfig"))

if __name__ == "__main__":
    app.run(host="0.0.0.0")