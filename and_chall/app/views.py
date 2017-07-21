from flask import render_template, request,  jsonify, json
import os

from app import app

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/register')
def register():
	return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
        if request.method == 'POST':
		if valid_login(request.form['username'],request.form['password']):
            		return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
	return render_template('login.html', error=error)

@app.route('/account')
def account():
	return render_template("account.html")


@app.route('/registerUser', methods=['POST'])
def registerUser():
	if request.method =='POST':
		user =  request.form['username'];
    		password = request.form['password'];
		if user=="" or password=="":
			return render_template('register.html')
		else:
			data={}
			data={user:password}
    			with open('file.txt', 'w') as f:
        			json.dump(data, f)
    			return render_template('account.html')


@app.route('/loginUser', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
	return render_template('register.html')
    else:
        flash('wrong password!')
    return home()













@app.route('/sample')
def sample():
	return render_template("sample.html")






@app.route('/json1',methods=['GET','POST'])
def json1():
   with open(os.path.join(os.path.dirname(__file__),"samp.json"), 'r') as json_data:
   	j = json.load(json_data)
   return j











