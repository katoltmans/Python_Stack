from flask import Flask, render_template
app=Flask(__name__)


#initial load page - 8 x 8 checkerboard
@app.route('/')
def checkerboard():
    return render_template('index.html', rows=8, columns=8, color1='red', color2='black')

#initial load page - 8 x given number of rows checkerboard
@app.route('/<int:rows>')
def checkerboard2(rows):
    return render_template('index.html', rows = rows, columns=8, color1='red', color2='black')

#initial load page - given number of columns x given number of rows checkerboard
@app.route('/<int:rows>/<int:columns>')
def checkerboard3(rows, columns):
    return render_template('index.html', rows = rows, columns=columns, color1='red', color2='black')

#initial load page - given number of columns x given number of rows checkerboard with given color1
@app.route('/<int:rows>/<int:columns>/<string:color1>/<string:color2>')
def checkerboard4(rows, columns, color1, color2):
    return render_template('index.html', rows = rows, columns=columns, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)