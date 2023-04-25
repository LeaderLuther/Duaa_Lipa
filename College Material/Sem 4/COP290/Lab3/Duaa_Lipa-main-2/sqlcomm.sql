CREATE TABLE user_table(
	User_ID INT NOT NULL AUTO_INCREMENT,
    Username VARCHAR(50) NOT NULL,
    User_description VARCHAR(1024),
	FirstName VARCHAR(256) NOT NULL,
    LastName VARCHAR(256) NOT NULL,
    Email VARCHAR(256),
    Gender VARCHAR(20) NOT NULL,
    Food VARCHAR(50),
    Drink VARCHAR(50),
    Smoke VARCHAR(50),
    Education VARCHAR(50),
    Relationship_type VARCHAR(20),
    Sexual_orientation VARCHAR(20),
    Sexual_preference VARCHAR(20),
    Age INT NOT NULL,
    Photolink1 VARCHAR(1024),
    Photolink2 VARCHAR(1024),
    Photolink3 VARCHAR(1024),
    PRIMARY KEY (User_ID)
);

CREATE TABLE likes_table(
    Likedby_User_ID INT NOT NULL,
    Likedwho_User_ID INT NOT NULL,
    Like_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE matches_table(
    Matchedby_User_ID INT NOT NULL,
    Matchedwho_User_ID INT NOT NULL,
    Matched_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE messages_table(
    Sender_User_ID INT NOT NULL,
    Receiver_User_ID INT NOT NULL,
    Message_Text VARCHAR(256) NOT NULL,
    Text_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


SELECT user_table.*, likes_table.Time_liked, likes_table.Date_liked 
  FROM user_table
   INNER JOIN likes_table
   ON user_table.User_ID = likes_table.Likedwho_User_ID AND likes_table.Likedby_User_ID = :val
   
   
   
   insert into likes_table (Likedby_User_ID, Likedwho_User_ID)
values (1, 7);