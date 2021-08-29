from flask import Flask, render_template
import pymysql as pymysql
from flask import request, redirect, session

app = Flask(__name__)
# Global connection


app.secret_key = 'ndsb'


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        admission = str(request.form['admission'])
        fullname = str(request.form['fullname'])
        password = str(request.form['password'])
        email = str(request.form['email'])
        standard = str(request.form['standard'])
        phone = str(request.form['phone'])
        gender = str(request.form['gender'])
        age = str(request.form['age'])

        conn = pymysql.connect("localhost", 'root', '', 'happyschool')
        cursor = conn.cursor()

        insert_query = "INSERT INTO `registration_table`(`admission`, `fullname`, `password`, `email`, `standard`, `phone`, 'gender', 'age' ) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(insert_query,
                          (admission, fullname, password, email, standard, phone, gender, age))
            conn.commit()
            return render_template('registration.html', msg='Registration successful')
        except:
            conn.rollback()
            return render_template('registration.html', msg='booking failed')

    else:
        return render_template('registration.html')
    # else:
    #     return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        fullname = request.form['fullname']
        password = request.form['password']

        # create a connection
        conn = pymysql.connect('localhost', 'root', '', 'happy_school')
        cursor = conn.cursor()

        select_query = "SELECT fullname, password FROM registration_table WHERE fullname=%s AND password = %s "
        cursor.execute(select_query, (fullname, password))
        if cursor.rowcount == 0:
            return render_template('login.html', error_msg='no student found, login failed')
        elif cursor.rowcount == 1:
            session['fullname'] = fullname
            # return render_template('login.html', success_msg = 'Account found, Login successful')
            return redirect('/checkin')
        elif cursor.rowcount > 1:
            return render_template('login.html', acc_error='Too many students detected')
        else:
            return render_template('login.html', error='something went wrong')
    else:
        return render_template('login.html')


@app.route('/Calculation', methods=['POST', 'GET'])
def calculation():
    if request.method == 'POST':
        fullname = str(request.form['fullname'])
        standard = str(request.form['standard'])
        admission = str(request.form['admission'])
        gender = str(reuest.form['gender'])
        mathematics = str(request.form['mathematics'])
        english = str(request.form['english'])
        kiswahili = str(request.form['kiswahili'])
        science = str(request.form['science'])
        social = str(request.form['social'])

        # create a connection
        conn = pymysql.connect('localhost', 'root', '', 'happyschool', )
        cursor = conn.cursor()

        insert_query = "INSERT INTO 'calculation_table' ('fullname', 'standard', 'admission', 'gender', " \
                       "'mathematics', 'english', 'kiswahili', 'science', 'social' ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s," \
                       "%s) "
        if insert_query:
            cursor.execute(insert_query,
                           (fullname, standard, admission, gender, mathematics, english, kiswahili, science, social))
            conn.commit()
            return render_template('calculator.html', msg='Entry successful')
        else:
            conn.rollback()
            return render_template('calculator.html', msg='Entry failed')
    else:
        return render_template('calculator.html')


if __name__ == '__main__':
    app.run(debug=True)
