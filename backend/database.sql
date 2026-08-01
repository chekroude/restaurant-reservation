-- Base de données : restaurant_reservation

CREATE DATABASE IF NOT EXISTS restaurant_reservation;
USE restaurant_reservation;

-- users : les clients qui réservent
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- restaurants : les restaurants disponibles
CREATE TABLE restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    city VARCHAR(100) NOT NULL,
    description TEXT,
    capacity INT NOT NULL DEFAULT 20
);

-- reservations : le lien entre un user et un restaurant
CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    restaurant_id INT NOT NULL,
    reservation_date DATE NOT NULL,
    reservation_time TIME NOT NULL,
    guests INT NOT NULL,
    status VARCHAR(20) DEFAULT 'confirmed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);

-- Données de test pour ne pas partir d'une DB vide
INSERT INTO restaurants (name, city, description, capacity) VALUES
('Le Petit Gourmet', 'Nouakchott', 'Cuisine française raffinée', 30),
('Sahara Grill', 'Nouakchott', 'Spécialités grillées locales', 50),
('Ocean View', 'Nouadhibou', 'Fruits de mer face à l''océan', 25);
