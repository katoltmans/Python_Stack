from flask import Flask #import flask
app=Flask(__name__)  #create new instance called app

@app.route('/') #Default Route - will say Hello World
def helloWorld():
    return 'Hello World!'

@app.route('')

if __name__=="__main__":
    app.run(debug=True) #Run app in debug mode
