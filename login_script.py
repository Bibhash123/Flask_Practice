from flask import Flask, request, url_for,redirect
import cryptography
import json
app = Flask(__name__)
app.env='development'

@app.route('/success/<name>')
def success(name):
    return "Welcome %s"%name
@app.route('/fail/<name>')
def fail(name):
    return "Incorrect password for username %s"%name

@app.route('/login', methods=['POST','GET'])  #post method to get form data #get sends data to server in unencrypted form
def login():
    with open('c:/users/bibhash/desktop/flask/password.json','r') as fp:
        passwords=json.load(fp)
        
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        if password==passwords[username]:
            print(1)
            return redirect(url_for('success',name=username))
        else:
            return redirect(url_for('fail',name=username))
    
        
if __name__=='__main__':
    app.run(debug=True,use_reloader=False,host="127.0.0.1",port="5000",ssl_context='adhoc')
    
        
