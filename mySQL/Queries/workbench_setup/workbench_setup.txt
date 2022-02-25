USE carrier_schema;

-- Create = Insert
SELECT * FROM carriers;
SELECT * FROM flights;

INSERT INTO flights (number, starting_city, ending_city, carrier_id)
VALUES (450, 'Denver', 'Orlando', 11);

SELECT * FROM flights;

-- Read = SELECT
SELECT * FROM carriers;

SELECT * FROM carriers 
ORDER BY year_founded;

-- Update = UPDATE
Select * FROM flights;

UPDATE flights SET starting_city = 'Las Vegas', ending_city = 'Chicago'
WHERE flights.id = 20;


-- Delete = DELETE

DELETE FROM flights 
WHERE flights.id = 21;

SELECT * FROM flights;