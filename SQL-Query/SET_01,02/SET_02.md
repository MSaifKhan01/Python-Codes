16.
CREATE TABLE Restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3, 2),
    delivery_available BOOLEAN
);


17.

INSERT INTO Restaurants (name, cuisine_type, location, average_rating, delivery_available)
VALUES
    ('Restaurant A', 'Italian', 'City A', 4.5, TRUE),
    ('Restaurant B', 'Chinese', 'City B', 3.8, FALSE),
    ('Restaurant C', 'Mexican', 'City C', 4.2, TRUE),
    ('Restaurant D', 'Indian', 'City A', 4.0, TRUE),
    ('Restaurant E', 'Japanese', 'City B', 4.7, TRUE);


18. 
SELECT * FROM Restaurants
ORDER BY average_rating DESC;


19.

SELECT * FROM Restaurants
WHERE delivery_available = TRUE AND average_rating > 4;


20.
SELECT * FROM Restaurants
WHERE cuisine_type IS NULL OR cuisine_type = '';


21.

SELECT COUNT(*) FROM Restaurants WHERE delivery_available=true

22.
SELECT * FROM Restaurants
WHERE location LIKE '%New York%';
23.

SELECT AVG(average_rating) AS average_average_rating
FROM Restaurants;


24.

SELECT * FROM Restaurants ORDER BY average_rating DESC LIMIT 5;


25.
delete FROM Restaurants where id = 3;