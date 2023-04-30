from flask import Flask, render_template, request, redirect, url_for, flash
import database
from database import engine
from sqlalchemy import create_engine, text
import datetime

app = Flask(__name__)

global x
app.secret_key = 'dua_lipa'
x = -1
     
# @app.route("/likes/<username>")
# def your_likes(username):
#   PROFILE = database.load_profile_from_db(username)
#   LIKES = database.load_likes()
#   return render_template('n-e-w-your-likes.html', likes = LIKES, profile = PROFILE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/signup",methods=['GET','POST'])
def signup():
  global x
  if request.method == 'POST' and request.form['submit_button'] == 'section2':
     with engine.connect() as conn:
        var1 = conn.execute(text("INSERT INTO user_table (User_ID,Username,User_description,FirstName,LastName,Email,Gender,Food,Drink,Smoke,Education,Relationship_type,Sexual_orientation,Sexual_preference,Age,Photolink1,Photolink2,Photolink3,Password) VALUES (DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT)"))
        id_result = conn.execute(text("SELECT User_ID FROM user_table ORDER BY User_ID DESC LIMIT 1"))
        id = id_result.fetchone()[0]
        conn.commit()
        x=id
        print(x)
        print("signup")
     return redirect(url_for('name',id=id))
  # global x
  x = -1
  return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
   global x
   if request.method == "POST"and request.form['submit_button'] != 'section2':
      username = request.form['username']
      password = request.form['password']
      with engine.connect() as conn:
         id_result = conn.execute(text("SELECT User_ID FROM user_table WHERE Username = :username AND Password = :password"), {"username": username, "password": password})
         row = id_result.fetchone()
         if row is not None:
            # the query returned a row, so the result is not empty
            id = row[0]
            x=id
         else:
            flash('Incorrect username or password.','error')
            return redirect(url_for('login'))
      return redirect(url_for('show_for_you',user_id=id))
   return render_template('index.html')


@app.route('/process_button', methods=['POST'])
def process_button():
    if request.form['button'] == 'section1':
        return redirect(url_for('login'))#redirect to the method for the homepage
    else:
        return redirect(url_for('signup'))    


@app.route("/user_details/<int:id>",methods=['GET','POST'])
def user_details(id):
   if request.method=='POST' :
      email = request.form.get('email')
      password = request.form.get('password')
      with engine.connect() as conn:
        result1 = conn.execute(text("UPDATE user_table SET Email=:email WHERE User_ID=:id"), {'email': email, 'id': id, 'password': password})
        result2 = conn.execute(text("UPDATE user_table SET Password=:password WHERE User_ID=:id"), {'email': password, 'id': id, 'password': password})
        conn.commit()
      return redirect(url_for('show_for_you',user_id=id))
   if x==id :
    print(x)
    print("user_details")
    return render_template('DetailsAryan.html',id=id)
   else :
    print(x)
    print("failed")
    return "Error page not found"  

@app.route("/age/<int:id>", methods=['GET','POST'])
def age(id):
  if request.method=='POST':
      year = request.form.get("year")
      current_year = datetime.datetime.now().year
      #print(current_year)
      age=int(current_year)-int(year)
      with engine.connect() as conn:
          result1 = conn.execute(text("UPDATE user_table SET Age=:age WHERE User_ID=:id"), {'age': age, 'id': id})
          conn.commit()
      return redirect(url_for('gender',id=id))
  if x==id :
   return render_template('AgeAryan.html',id=id)
  else :
   return "Error page not found"

@app.route("/education/<int:id>", methods=['GET','POST'])
def education(id):
   if request.method=='POST':
      education = request.form.get("education")
      with engine.connect() as conn:
         result1 = conn.execute(text("UPDATE user_table SET Education=:education WHERE User_ID=:id"), {'education': education, 'id': id})
         conn.commit()
      return redirect(url_for('habits',id=id))
   if x==id :
    return render_template('EducationAryan.html',id=id)
   else :
    return "Error page not found"  

@app.route("/gender/<int:id>",methods=['GET','POST'])
def gender(id):
    if request.method=='POST' :
      gender = request.form.get("gender")
      orientation = request.form.get("orientation")
      looking_for = request.form.get("looking_for")
      with engine.connect() as conn:
         result1 = conn.execute(text("UPDATE user_table SET Gender=:gender WHERE User_ID=:id"), {'gender': gender, 'id': id})
         result2 = conn.execute(text("UPDATE user_table SET Sexual_orientation=:orientation WHERE User_ID=:id"), {'orientation': orientation, 'id': id})
         result3 = conn.execute(text("UPDATE user_table SET Sexual_preference=:looking_for WHERE User_ID=:id"), {'looking_for': looking_for, 'id': id})
         conn.commit()
      return redirect(url_for('education',id=id))
    if x==id:
      return render_template('GenderAryan.html',id=id)
    else :
      return "Error page not found"

@app.route("/habits/<int:id>",methods=['GET','POST'])
def habits(id):
    if request.method=='POST' :
      drinking = request.form.get("drinking")
      smoking = request.form.get("smoking")
      eating = request.form.get("eating")
      with engine.connect() as conn:
         result1 = conn.execute(text("UPDATE user_table SET Food=:eating WHERE User_ID=:id"), {'eating': eating, 'id': id})
         result2 = conn.execute(text("UPDATE user_table SET Drink=:drinking WHERE User_ID=:id"), {'drinking': drinking, 'id': id})
         result3 = conn.execute(text("UPDATE user_table SET Smoke=:smoking WHERE User_ID=:id"), {'smoking': smoking, 'id': id})
         conn.commit()
      return redirect(url_for('user_details',id=id))
    if x==id:
     return render_template('HabitsAryan.html',id=id)
    else :
     return "Error page not found"

@app.route("/name/<int:id>",methods=['GET','POST'])
def name(id):
   if request.method=='POST':
      first_name = request.form.get('first_name')
      last_name = request.form.get('last_name')
      username = request.form.get('username')
      with engine.connect() as conn:
        result1 = conn.execute(text("UPDATE user_table SET FirstName=:first_name WHERE User_ID=:id"), {'first_name': first_name, 'id': id})
        result2 = conn.execute(text("UPDATE user_table SET LastName=:last_name WHERE User_ID=:id"), {'last_name': last_name, 'id': id})
        result = conn.execute(text("SELECT * FROM user_table WHERE Username=:username"), {'username': username})
        user = result.fetchone()
        if user:
            flash('Username already exists in the database', 'error')
            return redirect(url_for('name',id=id))
        else:
            if username is not None:
                result3 = conn.execute(text("UPDATE user_table SET Username=:username WHERE User_ID=:id"), {'username': username, 'id': id})
        conn.commit()
      #cur=mysql.connection.cursor()
      #cur.execute(f"UPDATE user_table SET Email='{email}' WHERE User_ID='{id}'")
      #mysql.connection.commit()
      #cur.close()
      return redirect(url_for('age',id=id))
   if x==id:
    print("hello")
    return render_template('new_name.html',id=id)
   else :
    return "Error page not found"

@app.route('/prev_name/<int:id>', methods=['POST'])
def prev_name(id):
    if request.method=='POST':
        return redirect(url_for('signup'))#redirect to the method for the homepage
    else:
        return redirect(url_for('name'),id=id)    

@app.route('/prev_age/<int:id>', methods=['POST'])
def prev_age(id):
    if request.method=='POST' :
        return redirect(url_for('name',id=id))#redirect to the method for the homepage
    else:
        return redirect(url_for('age',id=id)) 

@app.route('/prev_habit/<int:id>', methods=['POST'])
def prev_habit(id):
    if request.method=='POST' :
        return redirect(url_for('education',id=id))#redirect to the method for the homepage
    else:
        return redirect(url_for('habits',id=id)) 
    
@app.route('/prev_gender/<int:id>', methods=['POST'])
def prev_gender(id):
    if request.method=='POST':
        return redirect(url_for('age',id=id))#redirect to the method for the homepage
    else:
        return redirect(url_for('gender',id=id)) 

@app.route('/prev_education/<int:id>', methods=['POST'])
def prev_education(id):
    if request.method=='POST' :
        return redirect(url_for('gender',id=id))#redirect to the method for the homepage
    else:
        return redirect(url_for('education',id=id)) 
    
@app.route('/prev_details/<int:id>', methods=['POST'])
def prev_details(id):
    if request.method=='POST' :
        return redirect(url_for('habits',id=id))#redirect to the method for the homepage
    else:
        return redirect(url_for('user_details',id=id))   
  
#utkarsh has done till here

@app.route("/<int:user_id>/likes/<username>")
def your_likes(user_id, username):
  USER = database.load_user_from_db(user_id)
  PROFILE = database.load_profile_from_db(username)
  LIKES = database.load_likes_from_db(user_id)
  if x==user_id:
   return render_template('n-e-w-your-likes.html', likes = LIKES, profile = PROFILE, user = USER, type = "likes")
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/likes")
def likes_default(user_id):
  USER = database.load_user_from_db(user_id)
  PROFILE = {}
  LIKES = database.load_likes_from_db(user_id)
  if LIKES is None:
    LIKES = []
  if x==user_id:
   return render_template('likes_starter.html', likes = LIKES, profile = PROFILE, user = USER, type = "likes")
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/likes", methods = ['POST'])
def update_likes(user_id):
  DATA = request.form
  rem_id = DATA['removed']
  if request.form.get('action1') == '':
  #if DATA['action1'] == '':
    print("yaha kyu aaya")
    #print(rem_id)
    
    database.remove_like_in_db(user_id, rem_id)
    
  if request.form.get('action2') == 'MATCH':
    print("yaha aaya")
    
    database.remove_like_in_db(user_id, rem_id)
    database.add_match_in_db(user_id, rem_id)
    database.add_match_in_db(rem_id, user_id)
    
  if request.form.get('action3') == 'Kiss':
    print("lesgoo?")
    
    database.send_like_to_db(user_id, rem_id)
    # USER = database.load_user_from_db(user_id)
    # DISPLAY = database.profiles_to_show_from_db(user_id)
    
  USER = database.load_user_from_db(user_id)
  PROFILE = {}
  LIKES = database.load_likes_from_db(user_id)
  if LIKES is None:
    LIKES = []
  if x==user_id:
   return render_template('likes_starter.html', likes = LIKES, profile = PROFILE, user = USER, type = "likes")
  else :
    return "Error page not found"
  
# @app.route("/<int:user_id>/profile")
# def show_self_profile(user_id):
#   USER = database.load_user_from_db(user_id)
#   if x==user_id:
#     return render_template('new-your-profile.html', user = USER)
#   else :
#     return "Error page not found"
    
@app.route("/<int:user_id>/profile", methods = ['GET', 'POST'])
def show_self_profile(user_id):
  if request.method == 'GET':
    if x == user_id:
      USER = database.load_user_from_db(user_id)
      return render_template('new-your-profile.html', user = USER)
    else:
      return "Error page not found"
  if request.method == 'POST':
    return redirect(url_for('signup'))
            
@app.route("/<int:user_id>/messages")
def messages_default(user_id):
  USER = database.load_user_from_db(user_id)
  PROFILE = {}
  MATCHES = database.load_matches_from_db(user_id)
  if MATCHES is None:
    MATCHES = []
  if x==user_id:
    return render_template('messages-starter.html', likes = MATCHES, profile = PROFILE, user = USER, type = "messages")
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/messages", methods = ['POST'])
def unmatched_profile_on_messages(user_id):
  DATA = request.form
  rem_id = DATA['removed']
  database.remove_match_in_db(user_id, rem_id)
  database.remove_match_in_db(rem_id, user_id)
  database.remove_messages_in_db(rem_id, user_id)
  database.remove_messages_in_db(user_id, rem_id)
  USER = database.load_user_from_db(user_id)
  PROFILE = {}
  MATCHES = database.load_matches_from_db(user_id)
  if MATCHES is None:
    MATCHES = []
  if x==user_id:
    return render_template('messages-starter.html', likes = MATCHES, profile = PROFILE, user = USER, type = "messages")
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/messages/<username>")
def your_messages(user_id, username):
  rec_id = database.get_userid_from_username(username)['User_ID']
  USER = database.load_user_from_db(user_id)
  PROFILE = database.load_profile_from_db(username)
  MATCHES = database.load_matches_from_db(user_id)
  if MATCHES is None:
    MATCHES = []
  SENT_MESSAGES = database.load_messages_from_db(user_id, rec_id)
  if SENT_MESSAGES is None:
    SENT_MESSAGES = []
  RECEIVED_MESSAGES = database.load_messages_from_db(rec_id, user_id)
  if RECEIVED_MESSAGES is None:
    RECEIVED_MESSAGES = []
  ALL_MESSAGES = SENT_MESSAGES + RECEIVED_MESSAGES
  ALL_MESSAGES = sorted(ALL_MESSAGES, key=lambda d: d['Text_datetime'])
  if x==user_id :
    return render_template('n-e-w-messages.html', likes = MATCHES, profile = PROFILE, user = USER, type = "messages", messages = ALL_MESSAGES, sender = user_id, receiver = rec_id)
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/messages/<username>", methods = ['POST'])
def send_messages(user_id, username):
  DATA = request.form
  print(DATA['message'])
  rec_id = database.get_userid_from_username(username)['User_ID']
  print(rec_id)
  database.send_text_to_db(user_id, rec_id, DATA['message'])
  USER = database.load_user_from_db(user_id)
  PROFILE = database.load_profile_from_db(username)
  MATCHES = database.load_matches_from_db(user_id)
  if MATCHES is None:
    MATCHES = []
  SENT_MESSAGES = database.load_messages_from_db(user_id, rec_id)
  if SENT_MESSAGES is None:
    SENT_MESSAGES = []
  RECEIVED_MESSAGES = database.load_messages_from_db(rec_id, user_id)
  if RECEIVED_MESSAGES is None:
    RECEIVED_MESSAGES = []
  ALL_MESSAGES = SENT_MESSAGES + RECEIVED_MESSAGES
  ALL_MESSAGES = sorted(ALL_MESSAGES, key=lambda d: d['Text_datetime'])
  if ALL_MESSAGES is None:
    ALL_MESSAGES = []
  if x==user_id :
    return render_template('n-e-w-messages.html', likes = MATCHES, profile = PROFILE, user = USER, type = "messages", messages = ALL_MESSAGES, sender = user_id, receiver = rec_id)
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/user/<username>")
def show_profile(user_id, username):
  PROFILE = database.load_profile_from_db(username)
  USER = database.load_user_from_db(user_id)
  if not PROFILE:
    return "Profile Does Not Exist", 404
  if x==user_id:
    return render_template('other-profile.html', profile = PROFILE, user = USER)
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/for_you")
def show_for_you(user_id):
  USER = database.load_user_from_db(user_id)
  DISPLAY = database.profiles_to_show_from_db(user_id)
  if x==user_id:
    print(x)
    print("yay")
    return render_template('n-e-w-for-you.html', user = USER, display = DISPLAY)
  else :
    print(x)
    print(user_id)
    print("hahhy")
    return "Error page not found"
  
@app.route("/<int:user_id>/for_you", methods = ['POST'])
def like_profile_for_you(user_id):
  DATA = request.form
  
  if request.form.get('like1') == 'Kiss':
    liked_id = DATA['User1']
    
  if request.form.get('like2') == 'Kiss':
    liked_id = DATA['User2']
    
  if request.form.get('like3') == 'Kiss':
    liked_id = DATA['User3']
    
  database.send_like_to_db(user_id, liked_id)
  
  USER = database.load_user_from_db(user_id)
  DISPLAY = database.profiles_to_show_from_db(user_id)
  if x==user_id:
    print(x)
    print("for_you")
    return render_template('n-e-w-for-you.html', user = USER, display = DISPLAY)
  else :
    print(x)
    print("failed")
    return "Error page not found"
  
@app.route("/<int:user_id>/help")
def show_faq(user_id):
  USER = database.load_user_from_db(user_id)
  if x==user_id:
    return render_template('f-a-q-amaiya.html', user = USER)
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/profile")
def show_your_profile(user_id):
  USER = database.load_user_from_db(user_id)
  if x==user_id:
    return render_template('new-your-profile.html', user = USER)
  else :
    return "Error page not found"
  
@app.route("/<int:user_id>/home")
def show_home(user_id):
  USER = database.load_user_from_db(user_id)
  DISPLAY = database.profiles_to_show_from_db(user_id)
  if x==user_id:
    return render_template('n-e-w-home.html', user = USER, display = DISPLAY)
  else :
    return "Error page not found"
    
@app.route("/<int:user_id>/home", methods = ['POST'])
def like_profile_home(user_id):
  DATA = request.form
  
  if request.form.get('like1') == 'Kiss':
    liked_id = DATA['User1']
    
  if request.form.get('like2') == 'Kiss':
    liked_id = DATA['User2']
    
  if request.form.get('like3') == 'Kiss':
    liked_id = DATA['User3']
    
  if request.form.get('search') == 'Search':
    # Execute the search commands here
    USER = database.load_user_from_db(user_id)
    drink_pref = request.form.get("drinks")
    edu_pref = request.form.get('edu')
    rel_pref = request.form.get('reltype')
    smoke_pref = request.form.get('smoke')
    
    print(drink_pref, edu_pref, rel_pref, smoke_pref)
    
    DISPLAY = database.selected_profiles_to_show_from_db(user_id, drink_pref, edu_pref, smoke_pref, rel_pref)
    #this display thing will change
    if x==user_id:
      print(x)
      print("home")
      return render_template('n-e-w-home.html', user = USER, display = DISPLAY)
    else :
      print(x)
      print("failed")
      return "Error page not found"
    
  database.send_like_to_db(user_id, liked_id)
  
  USER = database.load_user_from_db(user_id)
  DISPLAY = database.profiles_to_show_from_db(user_id)
  if x==user_id:
    print(x)
    print("home")
    return render_template('n-e-w-home.html', user = USER, display = DISPLAY)
  else :
    print(x)
    print("failed")
    return "Error page not found"
  
@app.route("/<int:user_id>/profile/edit_info")
def show_edit_info(user_id):
  USER = database.load_user_from_db(user_id)
  if x==user_id:
    return render_template('n-e-w-edit-info.html', user = USER)
  else :
    return "Error page not found"
  
# @app.route("/signup")
# def signup():
#   return render_template('index.html')
  
if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)
  
