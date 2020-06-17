SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;
DROP DATABASE IF EXISTS cities_app;

CREATE DATABASE cities_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE cities_app;

DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries
(
    id      INT NOT NULL AUTO_INCREMENT,
    country VARCHAR(100),
    PRIMARY KEY (id)
);

INSERT INTO countries(country) VALUES
('Россия'), ('Украина'), ('США'), ('Германия'), ('Китай');

CREATE TABLE cities
(
    id         INT AUTO_INCREMENT,
    country_id INT NOT NULL,
    city       VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (country_id) REFERENCES countries (id)
);
INSERT INTO cities(country_id, city) VALUES
(1, 'Москва'),(1, 'Казань'),(1, 'Севастополь'),(1,'Екатеринбург'),(1,'Киров'),
(1, 'Тула'),(1, 'Красноярск'),(1, 'Пермь'),(1,'Уфа'),(1,'Саратов'),(1, 'Ханты-Мансийск'),
(2,'Днепр'),(2,'Киев'),(2,'Донецк'),(2,'Харьков'),(2,'Одесса'),
(2,'Моспино'),(2,'Николаев'),(2,'Новая Одесса'),(2,'Орехов'),(2,'Первомайский'),
(3,'Калифорния'),(3,'Нью-Йорк'),(3,'Лос-Анжелес'),(3,'Чикаго'),(3,'Хьюстон'),
(3,'Аспен'),(3,'Чарльстон'),(3,'Седона'),(3,'Теллерайд'),(3,'Саванна'),
(4,'Гамбург'),(4,'Берлин'),(4,'Кёльн'),(4,'Эссен'),(4,'Мюнхен'),
(4,'Бахарах'),(4,'Альсфельд'),(4,'Миттенвальд'),(4,'Мельн'),(4,'Моншау'),
(5,'Чунцин'),(5,'Шанхай'),(5,'Тяньцзынь'),(5,'Дунгуань'),(5,'Пекин'),
(5,'Дунгуань'),(5,'Шэньчжэнь'),(5,'Чэнду'),(5,'Ухань'),(5,'Шэньян');