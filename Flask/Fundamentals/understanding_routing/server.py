from flask import Flask #import flask
app=Flask(__name__)  #create new instance called app

@app.route('/') #Default Route - will say Hello World
def helloWorld():
    return 'Hello World!'

@app.route('/dojo') # Add function - page will say "Dojo!"
def dojo():
    return 'Dojo!'

@app.route('/say/<name>/') #Add function to say name typed in URL
def say(name):
    return 'Hi ' + name + '!'

if __name__=="__main__":
    app.run(debug=True) #Run app in debug mode
