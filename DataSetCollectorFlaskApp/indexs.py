from flask import Flask, render_template, request, session, redirect
import pyrebase
import firebase
import configurations

app = Flask(__name__)
app.secret_key = "secret"

# Firebase configuration
config = {
    "apiKey": "AIzaSyB-Iwn3Q2rwvnfHpirclyvy5bPRXRoMmOY",
    "authDomain": "subjective-evaluation-22a92.firebaseapp.com",
    "databaseURL": "https://subjective-evaluation-22a92-default-rtdb.firebaseio.com",
    "projectId": "subjective-evaluation-22a92",
    "storageBucket": "subjective-evaluation-22a92.appspot.com",
    "messagingSenderId": "107563738360",
    "appId": "1:107563738360:web:0482e645f46b4015afc70d",
    "measurementId": "G-27P6QEZ327"
}
# Initialize Firebase app
firebase = pyrebase.initialize_app(config)

# Firebase Authentication
auth = firebase.auth()
db = firebase.database()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exam')
def Base_qstn_paper_set():
    return render_template('first.html')


@app.route('/signup', methods=['POST', 'GET'])
def signUp():
    print("PYTHON")
    if request.method == 'POST':
        # Get user details from the form
        email = request.form['email']
        password = request.form['password']

        try:
            # Create a new user with email and password
            user = auth.create_user_with_email_and_password(email, password)
            # Login user and store user id in session
            session['user'] = user['idToken']
            # Redirect to dashboard
            return redirect('/dashboard')
        except:
            # Display error message if there is any issue with user creation
            return render_template('signup.html', message="Unable to create account. Please try again.")
    else:
        return render_template('signup.html')


@app.route('/signin', methods=['POST', 'GET'])
def signIn():
    if request.method == 'POST':
        # Get user details from the form
        email = request.form['email']
        password = request.form['password']

        try:
            # Sign in user with email and password
            user = auth.sign_in_with_email_and_password(email, password)
            # Store user id in session
            session['user'] = user['idToken']
            # Redirect to dashboard
            return redirect('/dashboard')
        except:
            # Display error message if there is any issue with sign in
            return render_template('signin.html', message="Invalid email or password. Please try again.")
    else:
        return render_template('signin.html')


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        # Get user details using user id from session
        user = auth.get_account_info(session['user'])
        return render_template('dashboard.html', email=user['users'][0]['email'])
    else:
        # Redirect to signin if user is not logged in
        return redirect('/signin')


@app.route('/foo', methods=['POST', 'GET'])
def foo():
    if request.method == 'POST':
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']

        email = request.form['emailID']

        ans = {"a1": first, "a2": second, "a3": third, "email": email}

        result = db.child("/answers").push(ans)

        # authvar = firebsevar.auth()
        # print(authvar.current_user)
        # result = firebasevar.post('/answers/', data=ans, params={'print': 'pretty'},
        #                           headers={'X_FANCY_HEADER': 'VERY FANCY'})
        # print(result)
    return render_template('first.html')


@app.route('/signout')
def signOut():
    # Clear user id from session and sign out user
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
