from flask import Flask , render_template, request , flash , session
from flask_mysqldb import MySQL
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = "randomunknown"

#configure db . connecting to db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Dbmsproject#1987'
app.config['MYSQL_DB']='dbms'
#lets instanciate the object for MYSQL
mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/validate',methods=['POST'])
def login_val():
    _email = request.form['email']
    _password = request.form['password']
    #check the received values with the values that the user have entered during register 
    if '@' in _email:
        if _email and _password and request.method == 'POST':
            #check whether the user is already there or not
            conn = mysql.connection
            cursor = conn.cursor()
            sql = "SELECT * FROM register WHERE email=%s"
            sql_where = (_email,)
            cursor.execute(sql,sql_where)
            row = cursor.fetchone()
            if row:
                if _email == row[2] and _password == row[3]:
                    session['user_email'] = row[2]
                    cursor.close()
                    conn.close()
                    return redirect('/home')
                else:
                    flash('Password is incorrect !!')
                    return redirect('/login')
            else:
                flash('Invalid email/pass')
                return redirect('/login')
    else:
        flash('Incorrect Email')
        return redirect('/')
           

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_user', methods= ['POST'])
def adding_user():
    conn = None
    cursor = None
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    college = request.form['college']
    #user validation - now only for email if at the rate (@) is present ot not
    if('@' in email):
        if name and email and password and college and request.method == 'POST':
            conn = mysql.connection
            cursor = conn.cursor()
            sql_1 = "SELECT * FROM register WHERE email=%s"
            data_1=(email,)
            cursor.execute(sql_1,data_1)
            temp = cursor.fetchall()
            if temp:
                flash('Email ID already Exists')
                return redirect('/register')
            conn = mysql.connection
            cursor = conn.cursor()
            sql = "INSERT INTO register(name,email,password,college) VALUES(%s,%s,%s,%s)"
            data = (name,email,password,college,)
            
            cursor.execute(sql,data)
            conn.commit()
            flash('user added')
            return redirect('/')
    else:
        flash('Invalid email ID')
        return redirect('/register')

@app.route('/home')
def home():
    if 'user_email' in session:

        return render_template('home.html')
    return render_template('login.html')

@app.route('/shareexp')
def share_exp():
    return render_template('userexperience.html')

@app.route('/add_user_exp' , methods=['POST'])
def add_user_expe():
    companyname = request.form['companyname']
    experience = request.form['experience']
    # conn = mysql.connection()
    userid = session['user_email']
    conn = mysql.connection
    cursor = conn.cursor()
    sql = "INSERT INTO user_experience(name,experience,userid) VALUES(%s,%s,%s)"
    data = (companyname,experience,userid,)
    cursor.execute(sql,data)
    conn.commit()
    return redirect('/viewexp')

@app.route('/edit_user_exp_submit/<int:id>' , methods=['POST'])
def edit_user_expe_submit(id):
    temp1=id
    companyname = request.form['companyname']
    experience = request.form['experience']
    # conn = mysql.connection()
    userid = session['user_email']
    conn = mysql.connection
    cursor = conn.cursor()
    sql = "UPDATE user_experience SET name=%s,experience=%s WHERE sno=%s AND userid=%s"
    data = (companyname,experience,temp1,userid,)
    cursor.execute(sql,data)
    conn.commit()
    return redirect('/viewexp')

@app.route('/edit_user_exp/<int:id>')
def edit_user_experience(id):
    
    temp2=id
    
    return render_template("editexp.html",temp2=temp2)
    # return "home"

@app.route('/delete_user_exp/<int:id>')
def delete_user_experience(id):
    
    temp3=id
    userid = session['user_email']
    conn = mysql.connection
    cursor = conn.cursor()
    sql = "DELETE FROM user_experience WHERE sno=%s AND userid=%s"
    data = (temp3,userid,)
    cursor.execute(sql,data)
    conn.commit()
    return redirect('/viewexp')



@app.route('/viewexp')
def view_exp():
    conn = mysql.connection
    cursor = conn.cursor()
    sql = "SELECT * FROM user_experience"
    cursor.execute(sql,)
    posts = cursor.fetchall()
    conn.commit()

    
    return render_template('viewexperience.html',posts=posts)


@app.route('/help')
def help_others():
    return render_template('helpothers.html')

@app.route('/hiringnow')
def hiring_now():
    conn = mysql.connection
    cursor = conn.cursor()
    sql = "SELECT * FROM help_others"
    cursor.execute(sql,)
    posts = cursor.fetchall()
    conn.commit()

    
    return render_template('company.html',posts=posts)
    

@app.route('/help_others', methods=['POST'])
def help_other_submit():
    if request.method == 'POST':
        # companyname = request.form['companyname']
        # experience = request.form['experience']
        companyn = request.form['companyn']
        roleoffer = request.form['roleoffer']
        requirement = request.form['requirement']
        link = request.form['link']
        userid = session['user_email']
        conn = mysql.connection
        cursor = conn.cursor()
        sql = "INSERT INTO help_others(name,role,requirement,link,userid) VALUES(%s,%s,%s,%s,%s)"
        data = (companyn,roleoffer,requirement,link,userid)
        cursor.execute(sql,data)
        conn.commit()
        
        return redirect('/hiringnow')

# @app.route('/help_others_view', methods=['POST'])
# def view_other_view():
#     conn = mysql.connection
#     cursor = conn.cursor()
#     sql = "SELECT * FROM help_others;"
#     cursor.execute(sql,)
#     posts = cursor.fetchall()
#     conn.commit()

#     return "hello"
#     return redirect('/hiringnow',posts=posts)

@app.route('/edit_helpother/<int:id>')
def edit_helpother(id):
    temp2=id
    
    return render_template("edithelp.html",temp2=temp2)


@app.route('/edit_helpother_submit/<int:id>' , methods=['POST'])
def edit_helpother_submit(id):
    temp1=id
    companyn = request.form['companyn']
    role = request.form['roleoffer']
    requirement = request.form['requirement']
    link = request.form['link']
    userid = session['user_email']
    # conn = mysql.connection()
    userid = session['user_email']
    conn = mysql.connection
    cursor = conn.cursor()
    sql = "UPDATE help_others SET name=%s,role=%s,requirement=%s,link=%s WHERE sno=%s AND userid=%s"
    data = (companyn,role,requirement,link,temp1,userid,)
    cursor.execute(sql,data)
    conn.commit()
    return redirect('/hiringnow')


@app.route('/delete_helpother/<int:id>')
def delete_helpother(id):
    
    temp3=id
    userid = session['user_email']
    conn = mysql.connection
    cursor = conn.cursor()
    sql = "DELETE FROM help_others WHERE sno=%s AND userid=%s"
    data = (temp3,userid,)
    cursor.execute(sql,data)
    conn.commit()
    return redirect('/hiringnow')


@app.route('/logout')
def logout():
    session.clear()
    # flash('logout successful , login to continue')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)