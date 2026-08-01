from flask import Blueprint, request, jsonify
from app.database import get_db_connection

restaurant_bp = Blueprint("restaurants", __name__)


@restaurant_bp.route("/restaurants", methods=["GET"])
def list_restaurants():
    """Liste tous les restaurants, avec recherche optionnelle par ville."""
    city = request.args.get("city")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if city:
        cursor.execute("SELECT * FROM restaurants WHERE city LIKE %s", (f"%{city}%",))
    else:
        cursor.execute("SELECT * FROM restaurants")

    restaurants = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(restaurants), 200


@restaurant_bp.route("/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    """Détails d'un restaurant précis."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM restaurants WHERE id = %s", (restaurant_id,))
    restaurant = cursor.fetchone()
    cursor.close()
    conn.close()

    if not restaurant:
        return jsonify({"error": "Restaurant introuvable"}), 404
    return jsonify(restaurant), 200
