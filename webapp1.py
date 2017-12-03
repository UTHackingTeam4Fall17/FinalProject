from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
 
import itertools
 
app = Flask(__name__)
 
# config
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)
 
# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
 
# silly user model
class User(UserMixin):
 
    def __init__(self, ID, name, password):
        self.id = ID
        self.name = name
        self.password = password
       
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)
 
 
# create some users with ids 1 to 20      
names = ['michael', 'arnav', 'cindy', 'nick']
password = ['password', 'abc123', '123456', 'apple']
user_dict = dict(itertools.izip(names, password))
ids = [val + 1 for val in range(len(names))]
pairs = zip(ids, names, password)
users = {name: User(ID, name, password) for ID, name, password in pairs}
user_ids = {ID: User(ID, name, password) for ID, name, password in pairs}
 
 
# some protected url
@app.route('/welcome')
@login_required
def home():
    return Response("Hello World!")
 
def get_login_form(message):
    return Response('''
   <div>{}</div>
   <form action="" method="post">
       <p><input type=text name=username>
       <p><input type=password name=password>
       <p><input type=submit value=Login>
   </form>
   '''.format(message))
 
# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        if username in user_dict and user_dict[username] == password:
            user = users[username]
            login_user(user)
            #return redirect('/welcome')
            return Response('Hello World!')
        else:
            return get_login_form('Please try again')
    else:
        return get_login_form('Please login')

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    print 'userid', userid
    return user_ids[int(userid)]
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
