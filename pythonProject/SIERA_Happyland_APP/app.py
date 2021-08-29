from flask import Flask, render_template
import pymysql as pymysql
from flask import request, redirect, session



app = Flask(__name__)
#Global connection


app.secret_key='ndsb'
@app.route('/',methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        id_number = str(request.form['id_number'])
        username = str(request.form['username'])
        password = str(request.form['password'])
        email = str(request.form['email'])
        location = str(request.form['location'])
        phone = str(request.form['phone'])

        conn = pymysql.connect("localhost", 'root', '', 'siera_happyland')
        cursor = conn.cursor()

        insert_query = "INSERT INTO `registration`(`id_number`, `username`, `password`, `email`, `location`, `phone`) VALUES  (%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(insert_query, (id_number, username, password, email, location, phone))
            conn.commit()
            return render_template('registration.html', msg = 'Registration successful')
        except:
            conn.rollback()
            return render_template('Checkin.html', msg='booking failed')


    else:
         return render_template('registration.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #create a connection
        conn = pymysql.connect('localhost', 'root', '', 'siera_happyland')
        cursor = conn.cursor()

        select_query = "SELECT username, password FROM registration WHERE username=%s AND password = %s "
        cursor.execute(select_query, (username, password))
        if cursor.rowcount ==0:
            return render_template('login.html', error_msg = 'no account found, login failed')

        elif cursor.rowcount ==1:
            session['username'] = username
            #return render_template('login.html', success_msg = 'Account found, Login successful')
            return redirect('/checkin')
        elif cursor.rowcount>1:
            return render_template('login.html', acc_error = 'Too many accounts detected')
        else:
            return render_template('login.html', error = 'something went wrong')

    else:
        return render_template('login.html')
@app.route('/checkin', methods = ['POST', 'GET'])
def checkin():
    if 'username' in session:
        if request.method == 'POST':
            fullname = request.form['fullname']
            email = request.form['email']
            phone = request.form['phone']
            nationality = request.form['nationality']
            address = request.form['address']
            checkin_date = request.form['checkin_date']
            checkin_time = request.form['checkin_time']
            roomno = request.form['roomno']
            checkout_date = request.form['checkout_date']
            checkout_time = request.form['checkout_time']

            conn = pymysql.connect("localhost", 'root', '', 'siera_happyland')
            cursor = conn.cursor()

            insert_query = "INSERT INTO `checkin`(`fullname`, `email`, `phone`, `nationality`, `address`, `checkin_date`,`checkin_time`, `roomno`, `checkout_date`, `checkout_time` ) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            try:
                cursor.execute(insert_query, (fullname, email, phone, nationality, address, checkin_date, checkin_time, roomno, checkout_date, checkout_time))
                conn.commit()
                return render_template('Checkin.html', msg='checkin successful')
            except:
                conn.rollback()
                return render_template('Checkin.html', msg='checkin failed')



        else:
            return render_template('Checkin.html')

    else:
        return redirect('/login')

@app.route('/viewcheckin')
def viewcheckin():
    if 'username' in session:

        conn = pymysql.connect("localhost", "root", '', "siera_happyland")
        cursor = conn.cursor()

        sql_query = "SELECT * FROM checkin"
        cursor.execute(sql_query)
        if cursor.rowcount<1:
            return render_template('viewcheckin.html', msg = 'no record found, table is empty')
        else:
            #now we can get all the rows returned by the cursor
            rows = cursor.fetchall()
            #after getting the rows we need
            #to send all of the rows to the UI or the html page
            return render_template('viewcheckin.html', rows = rows)
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email_address', None)
    return redirect('/login')

@app.route('/search',methods=['POST','GET'])
def search():
    if "username" in session:

        if request.method=="POST":
            phone=int(request.form['phone'])
            con=makeConnection()
            cur = con.cursor()
            sql="select * from checkin where phone=%s"

            cur.execute(sql,(phone))
            if cur.rowcount==0:
                return  render_template("search.html",msg="No visitors was found")
            elif cur.rowcount==1:
                session['phone']=phone
                return render_template("search.html",rows=cur.fetchall())

            elif cur.rowcount>1:
                return render_template("search.html",msg="Multiple visitors found: can't proceed")
        else:
            return render_template("search.html")
    else:
        return redirect("/login")


@app.route('/check_out', methods=['POST', 'GET'])
def check_out():
    if request.method == 'POST':
        roomno = str(request.form['roomno'])

        # connection to database
        # the parameters("server","username","password","database")
        con = pymysql.connect("localhost", "root", "", "siera_happyland")
        cursor = con.cursor()
        sql = "UPDATE checkin SET roomno=00 where roomno = (%s)"

        try:
            # when connection is established successfully
            cursor.execute(sql, roomno)
            con.commit()
            return render_template("check_out.html", msg="You have checked-out successfully")
        except:
            # when a connection is not established
            con.rollback()
            return render_template("check_out.html", msg="There is a problem with checking-out")
    else:
        return render_template("check_out.html")


# @app.route('/regout', methods=['POST', 'GET'])
# def regout():
#     if request.method == 'POST':
#         username = str(request.form['username'])
#
#         # connection to database
#         # the parameters("server","username","password","database")
#         con = pymysql.connect("localhost", "root", "", "siera_project")
#         cursor = con.cursor()
#         sql = "delete from registration_table where username = (%s)"
#
#         try:
#             # when connection is established successfully
#             cursor.execute(sql, username)
#             con.commit()
#             return render_template("regout.html", msg="You have unregistered successfully")
#         except:
#             # when a connection is not established
#             con.rollback()
#             return render_template("regout.html", msg="There is a problem with checking-out")
#     else:
#         return render_template("regout.html")

def makeConnection():
  return pymysql.connect("localhost", "root", "", "siera_happyland", )



if __name__ == '__main__':
    app.run(debug=True)