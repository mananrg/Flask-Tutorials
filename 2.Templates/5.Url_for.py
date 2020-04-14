from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('4.home.html')

@app.route('/puppy/<name>') 
def puppy_name(name):
    return render_template('4.puppy.html',name=name)

if __name__=='__main__':
    app.run(debug=True)