-- 1. Average price by brand
select make,ROUND(AVG(price),2) from vehicles
group by make
order by price desc;

-- 2. Top 5 most expensive cars


-- 3. Average mileage by fuel type


-- 4. Price vs. car age trend (average per year)


-- 5. Most common drivetrain per brand
