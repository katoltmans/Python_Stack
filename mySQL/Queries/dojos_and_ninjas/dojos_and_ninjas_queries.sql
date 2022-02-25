SELECT * FROM mydb;

-- Create 3 new dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('Fists of Fury', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
('Tokyo Budokan',  CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
('Kyokushin Training Hall', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());

SELECT * FROM dojos;

-- Delete 3 dojos that wetre created
DELETE FROM dojos
WHERE id <= 6;

-- Create 3 more dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('Miyagi-Do', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
('Eagle Fang Karate', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
('Cobra Kai', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());

-- Add 3 ninjas to Miyagi-Do
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Samantha', 'LaRusso', 17, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 7),
('Eli - Hawk', 'Moskowitz', 17, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 7),
('Demetri', 'Alexopoulos', 17, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 7);

-- Add 3 ninjas to Eagle Fang Karate
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Samantha', 'LaRusso', 17, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 8),
('Eli - Hawk', 'Moskowitz', 17, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 8),
('Demetri', 'Alexopoulos', 17, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 8);

UPDATE ninjas SET first_name = 'Miguel', last_name = 'Diaz' 
Where id = 4;

UPDATE ninjas SET first_name = 'Mitch', last_name = 'Johnson', age = 16 
Where id = 5;

UPDATE ninjas SET first_name = 'Devon', last_name = 'Jones', age = 16
Where id = 6;

-- Add 3 ninjas to Cobra Kai
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('Robby', 'Keene', 16, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 9),
('Tory', 'Nichols', 17, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 9),
('Kenny', 'Payne', 13, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 9);

SELECT * FROM ninjas;

-- Retrieve all ninjas from the 1st dojo
SELECT first_name, ninjas.last_name, dojos.name 
FROM ninjas 
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.dojo_id = 7;


-- Retrieve all ninjas from the 1st dojo
SELECT first_name, ninjas.last_name, dojos.name 
FROM ninjas 
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.dojo_id = 9;

-- Retrieve the last ninja's dojo
SELECT first_name, last_name, dojos.name AS dojo_name
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
ORDER BY ninjas.id DESC LIMIT 1;
