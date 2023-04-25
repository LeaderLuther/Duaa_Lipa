-- CREATE DATABASE main;
USE main;

CREATE TABLE user_table(
	User_ID INT,
    User_description VARCHAR(1024),
	FirstName VARCHAR(256),
    LastName VARCHAR(256),
    Email VARCHAR(256),
    Gender_ID INT,
    Relationship_type_ID INT,
    Sexual_preference_ID INT,
    Age INT
);

-- CREATE TABLE male_table(
-- 	User_ID INT,
--     Gender_ID INT,
--     Relationship_type_ID INT,
--     Sexual_pref_ID INT
-- );

-- CREATE TABLE female_table(
-- 	User_ID INT,
--     Gender_ID INT,
--     Relationship_type_ID INT,
--     Sexual_pref_ID INT
-- );

-- CREATE TABLE transgender_table(
-- 	User_ID INT,
--     Gender_ID INT,
--     Relationship_type_ID INT,
--     Sexual_pref_ID INT
-- );

-- CREATE TABLE straight_table(
-- 	User_ID INT,
--     Gender_ID INT,
--     Relationship_type_ID INT,
--     Sexual_pref_ID INT
-- );

-- CREATE TABLE gay_table(
-- 	User_ID INT,
--     Gender_ID INT,
--     Relationship_type_ID INT,
--     Sexual_pref_ID INT
-- );

-- CREATE TABLE bisexual_table(
-- 	User_ID INT,
--     Gender_ID INT,
--     Relationship_type_ID INT,
--     Sexual_pref_ID INT
-- );

CREATE TABLE user_photos_table(
	User_ID INT,
    Photo1_ID INT,
    Photo2_ID INT,
    Photo3_ID INT
);

CREATE TABLE liked_profiles_table(
	Likedby_User_ID INT,
    Likedwho_User_ID INT,
    Time_liked TIME,
    Date_liked DATE
);

CREATE TABLE conversations_table(
	User1_ID INT,
    User2_ID INT,
    Conversation_ID INT,
    Time_started TIME
);

CREATE TABLE messages_table(
	Conversation_ID INT,
    Message_ID INT,
    User_sent_ID INT,
    User_received_ID INT,
    Time_sent_ID INT,
    Message_content VARCHAR(256)
);

