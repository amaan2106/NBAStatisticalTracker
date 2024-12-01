import csv

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3

app = Flask(__name__)

#connect to the SQL Database
con = sqlite3.connect("database.db")
cur = con.cursor()

#Creating as table to store user info
sql_query = """ 
    CREATE TABLE IF NOT EXISTS User
    (
        username TEXT PRIMARY KEY,
        password TEXT
    )
"""
cur.execute(sql_query)

sql_query_votes = """ 
    CREATE TABLE IF NOT EXISTS Votes
    (
        username TEXT,
        mvp_vote TEXT,
        dpoy_vote TEXT,
        six_vote TEXT,
        roty_vote TEXT,
      FOREIGN KEY (username) references User(username)
    )
"""
cur.execute(sql_query_votes)
  
@app.route('/')
def home():
  # Open the CSV file and read its contents
  with open('nba_players.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    players = list(reader)[:50]

  # Pass the list of players to the Jinja2 template for rendering

  return render_template('home.html', players=players)


@app.route('/load_more')
def load_more():
  page = int(request.args.get('page'))
  start_index = (page - 1) * 50
  end_index = start_index + 50

  with open('nba_players.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    players = list(reader)
  return jsonify(players[start_index:end_index])

@app.route('/api/leaders', methods=['POST', 'GET'])
def leaders():
  if (request.method == "POST"):
    try:
      con = sqlite3.connect('database.db')
      cur = con.cursor()
      cur.execute("SELECT COUNT(*) FROM Votes WHERE username=?",(session['currentUser'],))
      previous_votes = cur.fetchone()[0]
      if previous_votes > 0:
        # User has already voted
        flash('You have already voted, you cannot vote again!')
        return redirect(url_for("leaders"))
      else:
        mvp_vote = request.form['mvp_vote']
        dpoy_vote = request.form['dpoy_vote']
        six_vote = request.form['six_vote']
        roty_vote = request.form['roty_vote']
        sql_query_votes = "INSERT INTO Votes VALUES ('"
        sql_query_votes += session['currentUser'] + "','" + mvp_vote + "','" + dpoy_vote + "','" + six_vote + "','" + roty_vote + "')"
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(sql_query_votes)
        con.commit()
        flash("You have succesfully submitted your votes!")
        return redirect(url_for("leaders"))
    except KeyError:
      flash("Oops, something went wrong. Please make sure you are logged in and have selected a player for each category before submitting!")
      return redirect(url_for("leaders"))
  else:
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE mvp_vote='Jokic'")
    count_mvp_jokic = cur.fetchone()[0]
    
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE mvp_vote='Embiid'")
    count_mvp_embiid = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE mvp_vote='Antentokounmpo'")
    count_mvp_antentokounmpo = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE mvp_vote='Tatum'")
    count_mvp_tatum = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE mvp_vote='Sabonis'")
    count_mvp_sabonis = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE dpoy_vote='Jackson'")
    count_dpoy_jackson = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE dpoy_vote='Lopez'")
    count_dpoy_lopez = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE dpoy_vote='Claxton'")
    count_dpoy_claxton = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE dpoy_vote='Adebayo'")
    count_dpoy_adebayo = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE dpoy_vote='Antentokounmpo'")
    count_dpoy_antentokounmpo = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE six_vote='Brogdon'")
    count_six_brogdon = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE six_vote='Quickley'")
    count_sin_quickley = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE six_vote='Powell'")
    count_six_powell = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE six_vote='Maxey'")
    count_six_maxey = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE six_vote='Monk'")
    count_six_monk = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE roty_vote='Banchero'")
    count_roty_banchero = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE roty_vote='Williams'")
    count_roty_williams = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE roty_vote='Kessler'")
    count_roty_kessler = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE roty_vote='Ivey'")
    count_roty_ivey = cur.fetchone()[0]

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Votes WHERE roty_vote='Mathurin'")
    count_roty_mathurin = cur.fetchone()[0]
    return render_template("leaders.html", jokic_votes=count_mvp_jokic, embiid_votes=count_mvp_embiid, antentokounmpo_mvp_votes=count_mvp_antentokounmpo, tatum_votes=count_mvp_tatum, sabonis_votes=count_mvp_sabonis, jackson_votes=count_dpoy_jackson, lopez_votes=count_dpoy_lopez, claxton_votes=count_dpoy_claxton, adebayo_votes=count_dpoy_adebayo, antentokounmpo_dpoy_votes=count_dpoy_antentokounmpo, brogdon_votes=count_six_brogdon, quickley_votes=count_sin_quickley, powell_votes=count_six_powell, maxey_votes=count_six_maxey, monk_votes=count_six_monk, banchero_votes=count_roty_banchero, williams_votes=count_roty_williams, kessler_votes=count_roty_kessler, ivey_votes=count_roty_ivey, mathurin_votes=count_roty_mathurin)

  
@app.route('/logout')
def logout():
  session.pop("currentUser", None)
  return render_template("home.html")


@app.route('/api/register', methods=['POST', 'GET'])
def register():
  if (request.method == "POST"):
    username = request.form['username']
    password = request.form['password']
    try:
      #get the cursor (a pointer to the DB)
      sql_query = "INSERT INTO User VALUES ('"
      sql_query += username + "','" + password + "')"
      #execute query and commit results
      con = sqlite3.connect("database.db")
      cur = con.cursor()
      cur.execute(sql_query)
      con.commit()
      flash("User has been succesfully registered!")
      return render_template("login.html")
    except sqlite3.IntegrityError:
      flash("This username has already been taken. Try another one...",
            "error")
      return render_template("register.html")
  else:
    return render_template("register.html")


@app.route('/api/login', methods=['POST', 'GET'])
def login():
  if (request.method == "POST"):
    username = request.form['username']
    password = request.form['password']
    #Gets the cursor to point to DB
    sql_query = "SELECT username, password FROM USER WHERE "
    sql_query += "username = '" + username + "';"
    #execute the query and commit results:
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    rows = cur.execute(sql_query).fetchall()
    if (len(rows) == 0):
      flash("No User Found matching: " + username)
      return render_template("login.html")
    #row[0] contains username/password
    #row[0][1] is the password element
    elif (password != rows[0][1]):
      flash("Password entered was incorrect. Try again")
      return render_template("login.html")
    else:
      session['currentUser'] = username
      return render_template("home.html")
  else:
    return render_template("login.html")


@app.route('/teams')
def teams():
  return render_template("teams.html")

@app.route('/rosters')
def rosters():
  return render_template("rosters.html")

app.run(host='0.0.0.0', port=81)
