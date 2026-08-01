import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify

JWT_SECRET = os.getenv("JWT_SECRET")


def hash_password(password: str) -> str:
    """Transforme un mot de passe en clair en hash irréversible."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password: str, password_hash: str) -> bool:
    """Vérifie qu'un mot de passe correspond au hash stocké."""
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def generate_token(user_id: int) -> str:
    """Crée un token JWT valable 24h, prouvant l'identité de l'utilisateur."""
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def token_required(f):
    """
    Décorateur : protège une route pour qu'elle ne soit accessible
    qu'avec un token JWT valide (utilisateur connecté).
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            request.user_id = data["user_id"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expiré, reconnectez-vous"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token invalide"}), 401
        return f(*args, **kwargs)
    return decorated
