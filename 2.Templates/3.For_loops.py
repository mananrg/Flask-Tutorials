from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    name_list=['manan','deep','sai','khushbu']
    return render_template('3.For_loops.html',name_list=name_list)

if __name__ =="__main__":
    app.run()