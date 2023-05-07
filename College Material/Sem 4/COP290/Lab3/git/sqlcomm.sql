create database onekiss;
use onekiss;

CREATE TABLE likes_table (
	Likedby_User_ID int NOT NULL,
	Likedwho_User_ID int NOT NULL,
	Like_datetime timestamp NULL DEFAULT current_timestamp()
);

CREATE TABLE matches_table (
	Matchedby_User_ID int NOT NULL,
	Matchedwho_User_ID int NOT NULL,
	Matched_datetime timestamp NULL DEFAULT current_timestamp()
);

CREATE TABLE messages_table (
	Sender_User_ID int NOT NULL,
	Receiver_User_ID int NOT NULL,
	Message_Text varchar(256) NOT NULL,
	Text_datetime timestamp NULL DEFAULT current_timestamp()
);

CREATE TABLE user_table (
	User_ID int NOT NULL AUTO_INCREMENT,
	Username varchar(50) NOT NULL DEFAULT 'a',
	User_description varchar(1024),
	FirstName varchar(256) NOT NULL DEFAULT 'a',
	LastName varchar(256) NOT NULL DEFAULT 'a',
	Email varchar(256),
	Gender varchar(20) NOT NULL DEFAULT 'a',
	Food varchar(50),
	Drink varchar(50),
	Smoke varchar(50),
	Education varchar(50),
	Relationship_type varchar(20),
	Sexual_orientation varchar(20),
	Sexual_preference varchar(20),
	Age int NOT NULL DEFAULT '6',
	Photolink1 varchar(1024),
	Photolink2 varchar(1024),
	Photolink3 varchar(1024),
	Password varchar(50) NOT NULL DEFAULT 'a',
	PRIMARY KEY (User_ID)
);