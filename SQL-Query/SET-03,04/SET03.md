26) Problem: Create a Rides table / collection with the fields defined above.


CREATE TABLE Rides (
    ride_id INT PRIMARY KEY,
    ride_date DATE,
    start_location VARCHAR(100),
    end_location VARCHAR(100),
    distance DECIMAL(10, 2),
    duration_minutes INT,
    fare DECIMAL(10, 2)
) 


27)

db.Rides.insertMany([
    {
        ride_id: 1,
        ride_date: ISODate("2023-08-10"),
        start_location: "City A",
        end_location: "City B",
        distance: NumberDecimal("50.25"),
        duration_minutes: 60,
        fare: NumberDecimal("75.50")
    },
    {
        ride_id: 2,
        ride_date: ISODate("2023-08-11"),
        start_location: "City B",
        end_location: "City C",
        distance: NumberDecimal("40.75"),
        duration_minutes: 45,
        fare: NumberDecimal("60.75")
    },
    {
        ride_id: 3,
        ride_date: ISODate("2023-08-12"),
        start_location: "City C",
        end_location: "City D",
        distance: NumberDecimal("30.50"),
        duration_minutes: 35,
        fare: NumberDecimal("45.25")
    },
    {
        ride_id: 4,
        ride_date: ISODate("2023-08-13"),
        start_location: "City D",
        end_location: "City E",
        distance: NumberDecimal("65.20"),
        duration_minutes: 75,
        fare: NumberDecimal("95.80")
    },
    {
        ride_id: 5,
        ride_date: ISODate("2023-08-14"),
        start_location: "City E",
        end_location: "City F",
        distance: NumberDecimal("55.80"),
        duration_minutes: 70,
        fare: NumberDecimal("85.25")
    }
]);


**Problem 28:**

- **Prerequisite**: Understand how to order data in SQL 
- **Problem**: Write a query to fetch all rides, ordered by **`fare`** in descending order.


SELECT * FROM Rides ORDER BY fare DESC;

**Problem 29:**

- **Prerequisite**: Understand using math operations in SQL 
- **Problem**: Write a query to calculate the total **`distance`** and total **`fare`** for all rides.


SELECT SUM(distance) AS total_distance, SUM(fare) AS  total_fare FROM Rides;



**Problem 30:**

- **Prerequisite**: Understand how to use the AVG function in SQL 
- **Problem**: Write a query to calculate the average **`ride_time`** of all rides.


SELECT AVG(duration_minutes) AS average_ride_time FROM Rides;


**Problem 31:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) 
- **Problem**: Write a query to fetch all rides whose **`start_location`** or **`end_location`** contains 'Downtown'.

SELECT * FROM Rides WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';


**Problem 32:**

- **Prerequisite**: Understand how to use the COUNT function in SQL
- **Problem**: Write a query to count the number of rides for a given **`driver_id`**.


SELECT COUNT(*) AS ride_count FROM Rides WHERE driver_id = ride_id;


**Problem 33:**

- **Prerequisite**: Understand data updating in SQL
- **Problem**: Write a query to update the **`fare`** of the ride with **`id`** 4.

UPDATE Rides SET fare = 5567 WHERE ride_id = 4;


**Problem 34:**

- **Prerequisite**: Understand using GROUP BY in SQL 
- **Problem**: Write a query to calculate the total **`fare`** for each **`driver_id`**.

SELECT driver_id, SUM(fare) AS total_fare FROM Rides GROUP BY driver_id;

**Problem 35:**

- **Prerequisite**: Understand data deletion in SQL 
- **Problem**: Write a query to delete the ride with **`id`** 2.

DELETE FROM Rides WHERE ride_id = 2;







