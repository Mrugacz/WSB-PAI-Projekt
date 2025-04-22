import os
from app import db, create_app

app = create_app(os.getenv("APP_CONFIG", "SyncedDB.config.DevelopmentConfig"))
with app.app_context():
    db.create_all()