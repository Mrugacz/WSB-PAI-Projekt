from flask_login import UserMixin
from datetime import datetime, UTC
from . import db, login_manager
from .utils import EnumUserRole


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).scalar()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pretty_name = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.Enum(EnumUserRole), nullable=False, default=EnumUserRole.USER)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(UTC))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(UTC))

    def __repr__(self):
        return f"User({self.id}, '{self.username}')"
