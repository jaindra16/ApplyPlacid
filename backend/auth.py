from functools import wraps
from flask import request, jsonify
import jwt
from models import User

SECRET_KEY = "your_secret_key"

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Unauthorized"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_id = data['user_id']
        except:
            return jsonify({"error": "Invalid token"}), 401
        return f(user_id=user_id, *args, **kwargs)
    return decorated_function

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        token = jwt.encode({'user_id': user.id}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
