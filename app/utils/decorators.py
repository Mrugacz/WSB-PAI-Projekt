from flask import redirect, url_for, flash
from flask_login import current_user
from functools import wraps
from .enums.enum_user_role import EnumUserRole


def admin_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user.role != EnumUserRole.ADMIN:
            flash("Unauthorized", "error")
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)

    return wrap
