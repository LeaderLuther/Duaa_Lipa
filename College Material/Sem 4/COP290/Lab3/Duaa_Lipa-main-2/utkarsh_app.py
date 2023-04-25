from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///user.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True ,nullable=True,default="unknown")
    password = db.Column(db.String(500), unique=True ,nullable=True,default="unknown")
    name=db.Column(db.String(500), nullable=True,default="unknown")
    email=db.Column(db.String(500), unique=True ,nullable=True,default="unknown")
    age=db.Column(db.Integer, nullable=True,default=69)
    gender=db.Column(db.Integer, nullable=True,default="unknown")
    description=db.Column(db.String(500), nullable=True,default="unknown")
    def __repr__(self) -> str:
        return f"{self.username} - {self.password}"

@app.route('/signup', methods=['GET','POST'])
def signup_page():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']
        user= User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print("peachy ass")
    #allTodo=User.query.all()
    return render_template('DetailsAryan.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            error = 'Invalid Credentials. Please try again.'
            print(error)
        else:
            return redirect(url_for('home'))
    return render_template('index.html', error=error)


@app.route('/home')
def home():
    # Get all users from the database and pass them to the template
    all_users = User.query.all()
    return render_template('index.html', all_users=all_users)
# @app.route('/show')
# def products():
#     allTodo = Todo.query.all()
#     print(allTodo)
#     return "This is a user page"



if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=8000)