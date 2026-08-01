from flask import Blueprint, request, jsonify
from app.database import get_db_connection
from app.utils.security import token_required

reservation_bp = Blueprint("reservations", __name__)


@reservation_bp.route("/reservations", methods=["POST"])
@token_required
def create_reservation():
    """Crée une réservation pour l'utilisateur connecté (token_required)."""
    data = request.get_json()
    restaurant_id = data.get("restaurant_id")
    date = data.get("date")
    time = data.get("time")
    guests = data.get("guests")

    if not all([restaurant_id, date, time, guests]):
        return jsonify({"error": "Tous les champs sont requis"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # On vérifie que le restaurant existe avant de réserver
    cursor.execute("SELECT id FROM restaurants WHERE id = %s", (restaurant_id,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return jsonify({"error": "Restaurant introuvable"}), 404

    cursor.execute(
        """INSERT INTO reservations (user_id, restaurant_id, reservation_date, reservation_time, guests)
           VALUES (%s, %s, %s, %s, %s)""",
        (request.user_id, restaurant_id, date, time, guests)
    )
    conn.commit()
    reservation_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({"message": "Réservation confirmée", "reservation_id": reservation_id}), 201


@reservation_bp.route("/reservations/history", methods=["GET"])
@token_required
def reservation_history():
    """Historique des réservations de l'utilisateur connecté."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """SELECT r.id, r.reservation_date, r.reservation_time, r.guests, r.status,
                  res.name AS restaurant_name, res.city
           FROM reservations r
           JOIN restaurants res ON r.restaurant_id = res.id
           WHERE r.user_id = %s
           ORDER BY r.reservation_date DESC""",
        (request.user_id,)
    )
    history = cursor.fetchall()
    cursor.close()
    conn.close()

    # MySQL renvoie la date en objet `date` et l'heure en `timedelta` :
    # Flask ne peut pas les convertir en JSON directement, donc on les
    # transforme en texte lisible avant de répondre.
    for row in history:
        row["reservation_date"] = str(row["reservation_date"])
        row["reservation_time"] = str(row["reservation_time"])

    return jsonify(history), 200
