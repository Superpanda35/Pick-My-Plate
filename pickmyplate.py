from flask import Flask
from flask import render_template, request
from form import Form
import random
#from flask_mysqldb import MySQL
#import PyMySQL
from flaskext.mysql import MySQL
    
app=Flask(__name__)
app.secret_key='my secret key'
##app.config['MYSQL_HOST']='localhost'
##app.config['MYSQL_PASSWORD']='password'
##app.config['MYSQL_USER']='root'
##app.config['MYSQL_DB']='recipes'
##mysql=MySQL(app)
##db=PyMySQL.connect("localhost","root","password","recipes")
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PASSWORD']='password'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_DB']='recipes'
mysql = MySQL()
mysql.init_app(app)

@app.route('/',methods=['GET','POST'])
def choose():       
    recipes=['Black_bean_and_corn_quesdilla.txt','garlic_shrimp.txt','Grilled_Portobello.txt']
    print_recipes=['black_bean_quesdilla.html','garlic_shrimp.html','Grilled_Portobello.html']
    suggested_recipes=[]
    form=Form()
    meat=form.radiofield1.data
    dairy=form.radiofield2.data
    gluten=form.radiofield3.data
    num_meat=0
    num_gluten=0
    num_dairy=0
    try:
        cur=mysql.get_db().cursor()
        if meat=='yes':
            num_meat=1

        elif meat=='no':
            num_meat=-1
        if gluten=='yes':
            num_gluten=1

        elif gluten=='no':
            num_gluten=-1

        if dairy=='yes':
            num_dairy=1

        elif dairy=='no':
            num_dairy=-1
        boo1=False
        boo2=False
        boo3=False
        if num_meat==1 and num_dairy==1 and num_gluten==1:
            cur.execute('SELECT html FROM meals WHERE meat="yes" and dairy="yes" and gluten="yes"')
            suggested_recipes.append(cur.fetchone())
##    """
##    for x in range(0,len(recipes),1):
##                file=open(recipes[x],'r')
##                for line in file:
##                    if line=='-no meat':
##                        boo1=True
##                    if line== '-no dairy':
##                        boo2=True
##                    if line=='-no gluten':
##                        boo3=True
##                if boo1 and boo2 and boo3:
##                    suggested_recipes.append(print_recipes[x])
##                    """
        elif num_meat==1 and num_dairy==1 and num_gluten==-1:
            cur.execute('SELECT html FROM meals WHERE meat="yes" and dairy="yes" and gluten="no"')
            suggested_recipes.append(cur.fetchone())
##    """
##            for x in range(0,len(recipes),1):
##                file=open(recipes[x],'r')
##                for line in file:
##                    if line=='-no meat':
##                        boo1=True
##                    if line== '-no dairy':
##                        boo2=True
##                    if line=='-no gluten':
##                        boo3=True
##                if boo1 and boo2 and not boo3:
##                    suggested_recipes.append(print_recipes[x])
##                    """
        elif num_meat==1 and num_dairy==-1 and num_gluten==1:
            cur.execute('SELECT html FROM meals WHERE meat="yes" and dairy="no" and gluten="yes"')
            suggested_recipes.append(cur.fetchone())
##            """
##            for x in range(0,len(recipes),1):
##                file=open(recipes[x],'r')
##                for line in file:
##                    if line=='-no meat':
##                        boo1=True
##                    if line== '-no dairy':
##                        boo2=True
##                    if line=='-no gluten':
##                        boo3=True
##                if boo1 and not boo2 and boo3:
##                    suggested_recipes.append(print_recipes[x])
##                    """
        elif num_meat==-1 and num_dairy==1 and num_gluten==1:
            cur.execute('SELECT html FROM meals WHERE meat="no" and dairy="yes" and gluten="yes" ')
            suggested_recipes.append(cur.fetchone())
                                     
##            """
##            for x in range(0,len(recipes),1):
##                file=open(recipes[x],'r')
##                for line in file:
##                    if line=='-no meat':
##                        boo1=True
##                    if line== '-no dairy':
##                        boo2=True
##                    if line=='-no gluten':
##                        boo3=True
##                if not boo1 and boo2 and boo3:
##                    suggested_recipes.append(print_recipes[x])
##                    """
        elif num_meat==1 and num_dairy==-1 and num_gluten==-1:
            cur.execute('SELECT html FROM meals WHERE meat="yes" and dairy="no" and gluten="no"')
            suggested_recipes.append(cur.fetchone())
##
##            """
##            for x in range(0,len(recipes),1):
##                file=open(recipes[x],'r')
##                for line in file:
##                    if line=='-no meat':
##                        boo1=True
##                    if line== '-no dairy':
##                        boo2=True
##                    if line=='-no gluten':
##                        boo3=True
##                if boo1 and not boo2 and  not  boo3:
##                    suggested_recipes.append(print_recipes[x])
##                    """
        elif num_meat==-1 and num_dairy==1 and num_gluten==-1:
            cur.execute('SELECT html FROM meals WHERE meat="no" and dairy="yes" and gluten="no"')
            suggested_recipes.append(cur.fetchone())

            ##
##            """
##            for x in range(0,len(recipes),1):
##                file=open(recipes[x],'r')
##                for line in file:
##                    if line=='-no meat':
##                        boo1=True
##                    if line== '-no dairy':
##                        boo2=True
##                    if line=='-no gluten':
##                        boo3=True
##                if not boo1 and boo2 and not boo3:
##                    suggested_recipes.append(print_recipes[x])
##                    """
        elif num_meat==-1 and num_dairy==-1 and num_gluten==1:
            cur.execute('SELECT html FROM meals WHERE meat="no" and dairy="no" and gluten="yes"')
            suggested_recipes.append(cur.fetchone())
##
##                                     
##            """
##            for x in range(0,len(recipes),1):
##                file=open(recipes[x],'r')
##                for line in file:
##                    if line=='-no meat':
##                        boo1=True
##                    if line== '-no dairy':
##                        boo2=True
##                    if line=='-no gluten':
##                        boo3=True
##                if not boo1 and not boo2 and boo3:
##                    suggested_recipes.append(print_recipes[x])
##                    """
        elif num_meat==-1 and num_dairy==-1 and num_gluten==-1:
            cur.execute('SELECT html FROM meals WHERE meat="no" and dairy="no" and gluten="no"')
            suggested_recipes.append(cur.fetchone())
##
##            """
##            for x in range(0,len(recipes),1):
##                file=open(recipes[x],'r')
##                for line in file:
##                    if line=='-no meat':
##                        boo1=True
##                    if line== '-no dairy':
##                        boo2=True
##                    if line=='-no gluten':
##                        boo3=True
##                if not boo1 and not boo2 and not boo3:
##                    suggested_recipes.append(print_recipes[x])
##                    """
                               
        if request.method=='POST':
            return render_template(random.choice(suggested_recipes),form=form)
        else:
            return render_template('pickmyplate.html',form=form)
    except Exception as e:
        return str(e)
    
##    if request.method=="POST":
##        response=("<H1>Here are some recpies that might suit your liking</H1> Meat: %s" %(form.radiofield1.data))
##        response+=("<br> Dairy: %s" %(form.radiofield2.data))
##        response+=("<br> Gluten: %s" %(form.radiofield3.data))
##    return response
    
##@app.route('/register')
##def register_page():
##    try:
####        cur=db.cursor()
####        cursor.execute('SELECT meat FROM meals WHERE name="Simple Garlic Shrimp"')
####        return 'connected'
#####        cur.execute('SELECT meat FROM meals WHERE name="Simple Garlic Shrimp"')
####        conn = mysql.connection.connect()
####        cur = conn.cusror()
##        cur=mysql.get_db().cursor()
##        cur.execute("SELECT meat FROM meals WHERE name='Simple Garlic Shrimp'")
##        rv=cur.fetchone()
##        return str(rv)
##    except Exception as e:
##        return "ERROR:"+str(e)
if __name__=='__main__':
    app.run()
