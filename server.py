import mysql.connector
from flask import Flask, redirect, url_for, request,render_template

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="MyPythonDatabase"
)
mycursor = mydb.cursor()
app = Flask(__name__)



@app.route('/',methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'abanoob' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

@app.route('/indexLoged',methods = ['POST', 'GET'])
def home():
   return render_template('indexLoged.html')
  

@app.route('/addPatient',methods = ['POST', 'GET'])
def addPatient():
   if request.method == 'POST': ##check if there is post data
      name = request.form['name']
      Pid = request.form['id']
      age=request.form['age']
      department = request.form['department']
      doctorName=request.form['doctorName']
      room=request.form['room']
      surgeryDate=request.form['surgeryDate']
      try:
         print(name,department,Pid,age,room,doctorName,surgeryDate)
         sql1 = "INSERT INTO Patients (name, id, age, department, doctorName, room, surgeryDate) VALUES (%s,%s,%s,%s,%s,%s,%s)"
         val1 = (name,Pid,age,department,doctorName,room,surgeryDate)
         mycursor.execute(sql1, val1)
         mydb.commit()   
         return render_template('add.html',succ = "You are now Registered")
      except:
         return render_template('add.html',err="Something Went wrong ")
   else:
      return render_template('add.html')

@app.route('/viewPatient',methods = ['POST', 'GET'])
def viewPatients():
   if request.method == 'POST':
      return render_template('index.html')
   else:
      mycursor.execute("SELECT * FROM Patients")
      row_headers=[x[0] for x in mycursor.description] 
      myresult = mycursor.fetchall()
      data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
      }
      
      return render_template('view.html',data=data )

@app.route('/addEmp',methods = ['POST', 'GET'])
def addEmp():
   if request.method == 'POST': ##check if there is post data
      Ename = request.form['name']
      Eid = request.form['id']
      mail =request.form['mail']
      authority=request.form['authority']
      password=request.form['password']
      try:
         print(Ename,authority,Eid,mail,password)
         sql2 = "INSERT INTO Employees (name, id, mail,authority, password) VALUES (%s, %s,%s ,%s,%s)"
         val2 = (Ename,Eid,mail,authority ,password)
         mycursor.execute(sql2, val2)
         mydb.commit()   
         return render_template('addEmp.html',succ = "You are now Registered")  
      except:
         return render_template('addEmp.html',err="Something Went wrong ")   
   else:
      return render_template('addEmp.html')

@app.route('/viewEmp',methods = ['POST', 'GET'])
def viewEmp():
   if request.method == 'POST':
      return render_template('index.html')
   else:
      mycursor.execute("SELECT * FROM Employees")
      row_headers=[x[0] for x in mycursor.description] 
      Empresult = mycursor.fetchall()
      Empdata={
         'message':"data retrieved",
         'rec':Empresult,
         'header':row_headers
      }
      
      return render_template('viewEmp.html',Empdata=Empdata )
@app.route('/contactUs',methods = ['POST', 'GET'])
def contactUs():
   return render_template('contactUs.html')

@app.route('/teamMembers',methods = ['POST', 'GET'])
def teamMembers():
   return render_template('teamMembers.html')

if __name__ == '__main__':
   app.run()