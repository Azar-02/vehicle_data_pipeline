-- 1. Average price by brand
SELECT make, ROUND(AVG(price), 2) AS avg_price
FROM vehicles
GROUP BY make
ORDER BY avg_price DESC;

-- 2. Top 5 most expensive cars
SELECT name, make, model, year, price
FROM vehicles
ORDER BY price DESC
LIMIT 5;

-- 3. Average mileage by fuel type
SELECT fuel, ROUND(AVG(mileage), 2) AS avg_mileage
FROM vehicles
GROUP BY fuel
ORDER BY avg_mileage DESC;

-- 4. Price vs. car age trend (average per year)
SELECT car_age, ROUND(AVG(price), 2) AS avg_price
FROM vehicles
GROUP BY car_age
ORDER BY car_age ASC;

-- 5. Most common drivetrain per brand
SELECT make, drivetrain, COUNT(*) AS count
FROM vehicles
GROUP BY make, drivetrain
ORDER BY count DESC;
