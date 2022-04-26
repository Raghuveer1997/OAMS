from flask import Flask, render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'airplane'
app.config['MYSQL_PORT'] = 3307
 
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('Admin.html')
 
@app.route('/add_emp', methods = ['POST', 'GET'])
def addEmp():
    if request.method == 'GET':
        return render_template('AddEmp.html')
     
    if request.method == 'POST':
        ssn = request.form['ssn']
        name = request.form['name']
        address = request.form['address']
        salary = request.form['salary']
        union_no = request.form['union']
        phone_no = request.form['phno']
        erole = request.form['role']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s)''',(ssn,name,address,salary,union_no,phone_no,erole))
        mysql.connection.commit()
        cursor.close()
        msg = "Employee Added Successfully!!"
        return render_template('AddEmp.html',msg = msg)

@app.route('/show_emp', methods = ['POST', 'GET'])
def showEmp():
    try:
        cur = mysql.connection.cursor() 
        cur.execute(''' SELECT * FROM employee ''')
        data = cur.fetchall()
        return render_template('showEmp.html', data = data)
    except  mysql.connection.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

@app.route('/add_model', methods = ['POST', 'GET'])
def addModel():
    if request.method == 'GET':
        return render_template('model.html')
     
    if request.method == 'POST':
        model_no = request.form['model_no']
        capacity = request.form['capacity']
        weight = request.form['weight']
        
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO model VALUES(%s,%s,%s)''',(model_no,capacity,weight))
        mysql.connection.commit()
        cursor.close()
        msg = "Molde Added Successfully!!"
        return render_template('model.html',msg = msg)

@app.route('/show_model', methods = ['POST', 'GET'])
def showModel():
    try:
        cur = mysql.connection.cursor() 
        cur.execute(''' SELECT * FROM model ''')
        data = cur.fetchall()
        return render_template('showModels.html', data = data)
    except  mysql.connection.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

@app.route('/add_plane', methods = ['POST', 'GET'])
def addPlane():
    if request.method == 'GET':
        return render_template('plane.html')
     
    if request.method == 'POST':
        reg_no = request.form['reg_no']
        model_no = request.form['model_no']
      
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO plane VALUES(%s,%s)''',(reg_no,model_no))
        mysql.connection.commit()
        cursor.close()
        msg = "Plane Added Successfully!!"
        return render_template('plane.html',msg = msg)


@app.route('/show_plane', methods = ['POST', 'GET'])
def showPlane():
    try:
        cur = mysql.connection.cursor() 
        cur.execute(''' SELECT * FROM plane ''')
        data = cur.fetchall()
        return render_template('showPlanes.html', data = data)
    except  mysql.connection.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

@app.route('/add_exp', methods = ['POST', 'GET'])
def addExp():
    if request.method == 'GET':
        return render_template('Exp.html')
     
    if request.method == 'POST':
        model_no = request.form['model_no']
        ssn = request.form['ssn']
       
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO expert VALUES(%s,%s)''',(model_no,ssn))
        mysql.connection.commit()
        cursor.close()
        msg = "Expert Added Successfully!!"
        return render_template('Exp.html',msg = msg)

@app.route('/show_exp', methods = ['POST', 'GET'])
def showExp():
    try:
        cur = mysql.connection.cursor() 
        cur.execute(''' SELECT * FROM expert ''')
        data = cur.fetchall()
        return render_template('showExp.html', data = data)
    except  mysql.connection.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

@app.route('/add_tc', methods = ['POST', 'GET'])
def addTC():
    if request.method == 'GET':
        return render_template('TC.html')
     
    if request.method == 'POST':
        ssn = request.form['ssn']
        exam_date = request.form['exam_date']
        
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO trafficcontroller VALUES(%s,%s)''',(ssn,exam_date))
        mysql.connection.commit()
        cursor.close()
        msg = "Traffic Controller Added Successfully!!"
        return render_template('TC.html',msg = msg)
    return render_template('TC.html')

@app.route('/show_tc', methods = ['POST', 'GET'])
def showTC():
    try:
        cur = mysql.connection.cursor() 
        cur.execute(''' SELECT * FROM trafficcontroller ''')
        data = cur.fetchall()
        return render_template('showTC.html', data = data)
    except  mysql.connection.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    

@app.route('/add_tec', methods = ['POST', 'GET'])
def addTec():
    if request.method == 'GET':
        return render_template('Tec.html')
     
    if request.method == 'POST':
        ssn = request.form['ssn']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO technician VALUES(%s)''',(ssn))
        mysql.connection.commit()
        cursor.close()
        msg = "Technician Added Successfully!!"
        return render_template('Tec.html',msg = msg)

@app.route('/show_tec', methods = ['POST', 'GET'])
def showTec():
    try:
        cur = mysql.connection.cursor() 
        cur.execute(''' SELECT * FROM technician ''')
        data = cur.fetchall()
        return render_template('showTec.html', data = data)
    except  mysql.connection.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))


@app.route('/add_test', methods = ['POST', 'GET'])
def addTest():
    if request.method == 'GET':
        return render_template('Test.html')
     
    if request.method == 'POST':
        faa_no = request.form['faa_no']
        tname = request.form['tname']
        max_score = request.form['max_score']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO test VALUES(%s,%s,%s)''',(faa_no,tname,max_score))
        mysql.connection.commit()
        cursor.close()
        msg = "Test Added Successfully!!"
        return render_template('Test.html',msg = msg)
    return render_template('Test.html')

@app.route('/show_test', methods = ['POST', 'GET'])
def showTest():
    try:
        cur = mysql.connection.cursor() 
        cur.execute(''' SELECT * FROM test ''')
        data = cur.fetchall()
        return render_template('showTests.html', data = data)
    except  mysql.connection.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

@app.route('/About', methods = ['POST', 'GET'])
def About():
    return render_template('About.html')





 
app.run(host='localhost', port=5000)