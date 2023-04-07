from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dkf3sldkjfDF23fLJ3b'

#connect to the SQL Database
con = sqlite3.connect("database.db")
cur = con.cursor()

#Creating as table to store user info
sql_query=""" 
    CREATE TABLE IF NOT EXISTS User
    (
        username TEXT PRIMARY KEY,
        password TEXT
    )
"""
cur.execute(sql_query)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/draft')
def draft():
    return render_template("draft.html")
  
@app.route('/leaders')
def leaders():
    return render_template("leaders.html")

@app.route('/api/register', methods=['POST', 'GET'])
def register():
  if (request.method == "POST"):
    username=request.form['username']
    password=request.form['password']
    try:
      #get the cursor (a pointer to the DB)
      sql_query = "INSERT INTO User VALUES ('"
      sql_query += username + "','"+password +"')"
      #execute query and commit results
      con = sqlite3.connect("database.db")
      cur = con.cursor()
      cur.execute(sql_query)
      con.commit()
      flash("User has been succesfully registered!")
      return render_template("login.html")
    except sqlite3.IntegrityError:
      flash("This username has already been taken. Try another one...", "error")
      return render_template("register.html")
  else:
    return render_template("register.html")
    
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/teams')
def teams():
    return render_template("teams.html")




app.run(host='0.0.0.0', port=81)
