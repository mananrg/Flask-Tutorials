from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thank_you')
def thank_you():
    first=request.args.get('first')
    upper=any(c.isupper() for c in first)
    lower=any(c.islower() for c in first)
    digit=first[-1].isdigit()
    results=upper and lower and digit
    

    return render_template("thankyou.html",first=first,upper=upper,lower=lower,digit=digit,results=results)


@app.errorhandler(404)
def error(e):
    return render_template("error.html"),404

if __name__=="__main__":
    app.run(debug=True)