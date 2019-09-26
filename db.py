from flask import Flask
from flask.ext.mysqldb import MySQL
from flaskext.mysql import MySQL

app = Flask(__name__)


    # MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'recipes'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

@app.route('/register')
def index():
    cur=mysql.connection.cursor()
    
    
    conn=mysql.connect()
    
#    conn =mysql.connect(host="localhost",
#                          user="root",
#                          password="password",
#                          database="recipes")
    c=conn.cursor()
    return c, conn

