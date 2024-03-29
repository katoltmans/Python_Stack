SELECT * FROM friendships;

-- Create 6 new users

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Amy', 'Giver', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
('Eli', 'Byers', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
('Marky', 'Mark', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
('Big', 'Bird', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
('Kermit', 'The Frog', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
('Jim', 'Hopper', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());

SELECT * FROM users;

-- Make user 1 friends with users 2, 4 & 6
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 2, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(1, 4, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(1, 6, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());

-- Create rest of friendships
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (2, 1, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(2, 3, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(2, 5, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
(3, 2, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(3, 5, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(4, 3, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(5, 1, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(5, 6, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(6, 2, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()), 
(6, 3, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());

SELECT * FROM friendships;

-- Display friendship data in an organized table
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name 
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id;

-- Display users who are firends with user 1
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name 
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
WHERE users.id = 1;

-- Display count of all friendships
SELECT users.first_name, users.last_name, COUNT(friendships.friend_id) AS friends_count FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
GROUP BY users.first_name;

-- Display users with the most friends
Select users.first_name, users.last_name, COUNT(friendships.friend_id) AS friend_count FROM users
JOIN friendships ON users.id = friendships.user_id
JOIN users AS user2 ON user2.id = friendships.friend_id
GROUP BY users.first_name
ORDER BY friend_count DESC LIMIT 2;

-- Display friends of 3rd user in alphabetical order
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name 
FROM users
JOIN friendships ON users.id = friendships.user_id
Join users AS user2 ON user2.id = friendships.friend_id
WHERE users.id = 3
ORDER BY user2.first_name;

