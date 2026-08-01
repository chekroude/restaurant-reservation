from flask import Blueprint, request, jsonify
from app.database import get_db_connection
from app.utils.security import hash_password, check_password, generate_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # Validation basique des données reçues
    if not name or not email or not password:
        return jsonify({"error": "Tous les champs sont requis"}), 400
    if len(password) < 6:
        return jsonify({"error": "Mot de passe trop court (min 6 caractères)"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # On vérifie que l'email n'existe pas déjà
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return jsonify({"error": "Cet email est déjà utilisé"}), 409

    password_hash = hash_password(password)
    # Requête paramétrée (%s) : protège contre l'injection SQL
    cursor.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)",
        (name, email, password_hash)
    )
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()

    token = generate_token(user_id)
    return jsonify({"message": "Compte créé", "token": token}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email et mot de passe requis"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user or not check_password(password, user["password_hash"]):
        # Message volontairement vague : ne pas dire si c'est l'email ou le mdp qui est faux
        return jsonify({"error": "Email ou mot de passe incorrect"}), 401

    token = generate_token(user["id"])
    return jsonify({"message": "Connexion réussie", "token": token, "name": user["name"]}), 200
