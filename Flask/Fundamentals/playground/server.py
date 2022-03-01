from flask import Flask, render_template  # Import flask and render template
app = Flask(__name__)

#route for initial load screen
@app.route('/play')
def play():
    return render_template('index.html')


@app.route('/play/<int:num>')
def playNum(num):
    return render_template('index.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def playChangeColor(num, color):
    return render_template('index.html', num=num, color=color)

if __name__=="__main__":   # Run app directly
    app.run(debug=True)    # Run app in debug
