from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from app.routes.auth_routes import auth_bp
from app.routes.restaurant_routes import restaurant_bp
from app.routes.reservation_routes import reservation_bp

load_dotenv()

app = Flask(__name__)
CORS(app)  # Autorise le frontend (autre origine) à appeler cette API

# Enregistrement des routes, toutes préfixées par /api
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(restaurant_bp, url_prefix="/api")
app.register_blueprint(reservation_bp, url_prefix="/api")


@app.route("/")
def index():
    return {"message": "API Restaurant Reservation - OK"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
