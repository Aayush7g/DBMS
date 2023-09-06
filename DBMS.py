from flask import Flask, render_template, request, redirect, url_for, session, flash, json
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456789'
app.config['MYSQL_DB'] = 'contact'

mysql = MySQL(app)

app.secret_key = "yoursecretkey"
@app.route("/sign_up.html", methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        name = request.form['name']
        email_address = request.form['email_address']
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO sign_up ( name, email_address, password, repeat_password) VALUES (%s, %s, %s, %s)',(name, email_address, password, repeat_password))
        mysql.connection.commit()
    return render_template("sign_up.html")
@app.route("/")
@app.route("/sign_in.html")
def sign_in():
    if request.method == 'POST' and 'email_address' in request.form and 'password' in request.form:
        email_address = request.form['email_address']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM sign_in WHERE email_address = %s AND password = %s', (email_address, password,))
        account = cursor.fetchone()
        if account:
            session['email_address'] = account['email_address']
            session['password'] = account['email_address']
            return render_template('index.html')

    return render_template("sign_in.html")
@app.route("/home.html")
def Home():
    return render_template("Home.html")

@app.route("/about.html")
def about():
    return render_template("about.html")
@app.route("/contact.html",methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email_address = request.form['email_address']
        phone_number = request.form['phone_number']
        message = request.form['message']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO contacts ( name, email_address, phone_number, message) VALUES (%s, %s, %s, %s)',(name, email_address, phone_number, message))
        mysql.connection.commit()
    return render_template("contact.html")
@app.route("/post.html")
def post():
    return render_template("post.html")
app.run(debug=True)
