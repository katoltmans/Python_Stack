SELECT * FROM private_wall_schema.users;
SELECT * FROM private_wall_schema.friendships;

SELECT * FROM users LEFT JOIN friendships ON users.id = friendships.user_id;

SELECT * FROM friendships LEFT JOIN users ON users.id = friendships.user2_id WHERE user_id = 1;

SELECT * FROM messages LEFT JOIN friendships on friendships.user2_id = messages.users_id LEFT JOIN users ON friendships.user_id = users.id WHERE friendships.user_id = 2;