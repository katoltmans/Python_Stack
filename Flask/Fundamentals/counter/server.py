from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Shhhhhh..." #secret key set for security purposes

@app.route('/')
def start():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1 #Session to count clicks
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def count():
    print("Start count")
    return redirect('/')


@app.route('/plus_two', methods=['POST'])
def count2():
    print("Start count")
    session['count'] += 1 #Add 2 clicks each count
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    print("destroy")
    session.clear()  #clears the session and resets counter
    return redirect('/')  #Redirects user back to home route

if __name__=="__main__":
    app.run(debug=True)