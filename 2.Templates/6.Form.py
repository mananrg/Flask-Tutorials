from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('6.Index.html')

@app.route('/signup_form')
def signup_form():
    return render_template("6.Signup.html")

@app.route('/thank_you')
def thank_you():
    first=request.args.get('first')
    print(first)
    last=request.args.get('last')
    return render_template("6.Thankyou.html",first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("6.404.html"),404    
if __name__ =='__main__':
    app.run(debug=True)