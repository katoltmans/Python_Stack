#Import Flask
from flask import Flask, render_template, request, redirect, session
import random #Import ability to generate random numbers
app = Flask(__name__)
app.secret_key = "None shall pass"

#Routes
#Home page route
@app.route('/')
def home_page():
    if 'answer' not in session:
        session['answer']=random.randrange(0,100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def check_guess():
    session['user_guess'] = int(request.form["user_guess"])
    if session['answer']==session["user_guess"]:
        return redirect('/correct')
    else:
        return redirect('/')

@app.route('/correct')
def correct():
    return render_template("correct.html")

@app.route('/reset', methods=['POST'])
def clear_session():
    print("destroy")
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)