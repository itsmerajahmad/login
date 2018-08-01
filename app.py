from flask import Flask,render_template,url_for,request,redirect
import pymysql
from database import cur,con
app = Flask(__name__)

#index 1st
@app.route('/')
def index(): 
	 return render_template('user.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
'''
@app.route('/signup/',methods = ['POST','GET'])
def signup():
	guser=request.form['userr']
	gpsw=request.form['op']
	sql="insert into valid(uname,upass) values('%s','%s')"%(guser,gpsw)
	if cur.execute(sql):
		con.commit()
	else:
		return 'database operation failed.....'
'''
#login and validating user...
@app.route('/login',methods = ['POST', 'GET'])
def login():
	user=request.form['user']
	psw=request.form['pas']
	cur.execute("select uname,upass from valid")
	l=[1 for (i,j) in cur if user==i and psw==j]
	if l:
		return redirect(url_for('success',name = user))
	else:
		 return render_template('user.html',success='F')

if __name__ == '__main__':
   app.run(debug = True)