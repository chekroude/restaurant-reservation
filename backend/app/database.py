import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """
    Ouvre une nouvelle connexion à la base de données.
    On en crée une nouvelle à chaque requête (simple et sûr pour un MVP).
    """
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
