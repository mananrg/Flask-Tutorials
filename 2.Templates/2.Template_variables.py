from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def index():
    some_variable="Manan"
    return render_template("2.Template_variables.html",some_variable=some_variable)


if __name__=="__main__":
    app.run()