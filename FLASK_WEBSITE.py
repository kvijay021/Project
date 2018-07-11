from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#app.config['MySQL_HOST']='localhost'
#app.config['MySQL_USER']='root'
#app.config['MySQL_PASSWORD']=''
#app.config['MySQL_DB']='flaskapp'
#app.config['MYSQL_PORT']= 3306

#mysql = MySQL(app)


@app.route('/')
def index():
    return render_template("index.html")

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskapp'
app.config['MYSQL_PORT']= 3306

mysql = MySQL(app)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':

        contact_us = request.form
        name = contact_us['name']
        email = contact_us['email']
        mob = contact_us['mob']
        message = contact_us['message']
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM contact_us''')
        rv = cur.fetchall()
        return str(rv)
        #cur=mysql.connection.cursor()
        #cur.execute("insert into contact_us values(%s,%s,%s,%s)",(name,email,mob,message))
        #mysql.connection.commit()
        #cur.close()
        #return 'success'

    return render_template("contact.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
