SELECT * FROM mydb.users;

-- ALTER TABLE users RENAME COLUMN updatet_at TO updated_at;

-- Create 3 new users
INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ('Dion', 'Warren', 'dwarren@rd.com', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
('Nicole', 'Reese', 'nreese@rd.com', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
('Pat', 'Rollins', 'prollins@rd.com', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());

-- Retrieve all users
SELECT * FROM users;

-- Retrieve 1st user using email address
SELECT *FROM users
WHERE email = 'dwarren@rd.com';

-- Retrieve last user using id
SELECT * FROM users
WHERE users.id = 22;

-- Update users 22's last name to pancackes (I deleted a few records while figuring things out earleri id 3 = 22)
UPDATE users SET last_name = 'Pancakes'
WHERE id = 22;

-- Delete user 2 (21) from the database
DELETE FROM users
WHERE id = 21;

-- Sort users by first_name
SELECT first_name FROM users
ORDER BY first_name;

-- Sort users by first name in descending order
SELECT first_name FROM users
ORDER BY first_name DESC;
