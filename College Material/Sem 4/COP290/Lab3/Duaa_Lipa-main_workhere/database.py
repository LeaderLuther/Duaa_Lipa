from sqlalchemy import create_engine
from sqlalchemy.sql import text

#This is for connecting to our MySQL database
db_connection = "mysql+pymysql://gfxgrhxf9maut1s0ryko:pscale_pw_HgKBqBiaGayJJfuGLVEUVPbZkXwoitRRr6RXiXcBF0Q@aws.connect.psdb.cloud/one_kiss_website?charset=utf8mb4"
#db_connection="mysql+pymysql://root:duaa_lipa@localhost/onekiss"
#connect_args={
#        "ssl": {
#            "ca": "/etc/ssl/certs/ca-certificates.crt",
#	        }
#	    }	


	    
engine = create_engine(
	db_connection, 
  connect_args={
         "ssl": {
             "ca": "/etc/ssl/cert.pem",
          }
      } 
	)
    
def load_profiles():
  with engine.connect() as conn:
    result = conn.execute(text("select * from user_table"))
    likes = []
    for row in result.all():
      # likes.append(dict(row))
      likes.append(row._asdict())
    return likes
    
def load_profile_from_db(username):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM user_table WHERE Username = :val"), dict(val=username))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
      
def load_user_from_db(user_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM user_table WHERE User_ID = :user"), dict(user = user_id)
      )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
      
def load_likes_from_db(user_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT user_table.*, likes_table.Like_datetime FROM user_table INNER JOIN likes_table ON user_table.User_ID = likes_table.Likedby_User_ID AND likes_table.Likedwho_User_ID = :val"),
      dict(val = user_id)
      )
    likes = []
    rows = result.all()
    
    if len(rows) == 0:
      return None
      
    for row in rows:
      likes.append(row._asdict())
    return likes
    
def load_matches_from_db(user_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT user_table.*, matches_table.Matched_datetime FROM user_table INNER JOIN matches_table ON user_table.User_ID = matches_table.Matchedwho_User_ID AND matches_table.Matchedby_User_ID = :val"),
      dict(val = user_id)
      )
    matches = []
    rows = result.all()
    
    if len(rows) == 0:
      return None
      
    for row in rows:
      matches.append(row._asdict())
    return matches
    
def send_text_to_db(sender_id, receiver_id, mtext):
  with engine.connect() as conn:
    result = conn.execute(
      text("INSERT INTO messages_table (Sender_User_ID, Receiver_User_ID, Message_Text) VALUES (:s_id, :r_id, :txt)"),
      dict(
      s_id = sender_id,
      r_id = receiver_id,
      txt = mtext)
      )
    #conn.commit()
    
def get_userid_from_username(username):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT User_ID from user_table WHERE Username = :uname "),
      dict(
      uname = username)
      )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
      
def load_messages_from_db(sender_id, receiver_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * from messages_table WHERE Sender_User_ID = :s_id AND Receiver_User_ID = :r_id"),
      dict(
      s_id = sender_id,
      r_id = receiver_id)
      )
    
    messages = []
    rows = result.all()
    
    if len(rows) == 0:
      return None
      
    for row in rows:
      messages.append(row._asdict())
    return messages
    
def remove_like_in_db(user_id, removed_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("DELETE FROM likes_table WHERE LikedWho_User_ID = :u_id AND LikedBy_User_ID = :rem_id"),
      dict(u_id = user_id,
      rem_id = removed_id)
      )
    #conn.commit()
    
def remove_match_in_db(user_id, removed_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("DELETE FROM matches_table WHERE MatchedWho_User_ID = :u_id AND MatchedBy_User_ID = :rem_id"),
      dict(
      u_id = user_id,
      rem_id = removed_id)
      )
    #conn.commit()
    
def remove_messages_in_db(user_id, removed_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("DELETE FROM messages_table WHERE Sender_User_ID = :u_id AND Receiver_User_ID = :rem_id"),
      dict(
      u_id = user_id,
      rem_id = removed_id)
      )
    #conn.commit()
    
def add_match_in_db(user1_id, user2_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("INSERT INTO matches_table (Matchedby_User_ID, Matchedwho_User_ID ) VALUES (:u_id, :rem_id)"),
      dict(
      u_id = user1_id,
      rem_id = user2_id)
      )
    #conn.commit()
    
def profiles_to_show_from_db(user_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM user_table ORDER BY RAND() LIMIT 3")
      )
    users = []
    rows = result.all()
    
    if len(rows) == 0:
      return None
      
    for row in rows:
      users.append(row._asdict())
    return users
    
def selected_profiles_to_show_from_db(user_id, drink_pref, edu_pref, smoke_pref, rel_pref):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM user_table WHERE Education=:edu_pref AND Drink=:drink_pref AND Smoke=:smoke_pref AND Relationship_type=:rel_type ORDER BY RAND() LIMIT 3"),
      dict(
        edu_pref = edu_pref,
        drink_pref = drink_pref,
        smoke_pref = smoke_pref,
        rel_type = rel_pref)
      )
    users = []
    rows = result.all()
    
    if len(rows) == 0:
      return None
      
    for row in rows:
      users.append(row._asdict())
    return users    
    
def send_like_to_db(user_id, liked_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("INSERT INTO likes_table (Likedby_User_ID, Likedwho_User_ID) VALUES (:u_id, :l_id)"),
      dict(u_id = user_id, l_id = liked_id)
      )
    #conn.commit()

def get_photo_links(user_id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT Photolink1, Photolink2, Photolink3 FROM user_table WHERE user_id = :user_id"),
      dict(user_id = user_id)
    )
  result_set = result.fetchall()
  links = []
  for row in result_set:
    links.append(row._asdict())
  return links

# with engine.connect() as conn:
# 	result = conn.execute(text("select * from user_table"))
# 	print(type(result))
# 	result_all = result.all()
# 	print(result_all[0]) #this is of sqlalchemy row type
# 	#we want to convert it into a python dictionary
# 	result_first = dict(result_all[0])
	
# 	result_dicts = []
# 	for row in result.all():
# 		result_dicts.append(dict(row))
# 	#this will create a dictionary of all the rows in the table
