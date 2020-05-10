from flask import Flask,render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import (StringField,TextField,TextAreaField,
                    RadioField,BooleanField,
                    SubmitField,DateTimeField,SelectField)
from wtforms.validators import DataRequired
app=Flask(__name__)
app.config['SECRET_KEY']='mykey'
class InfoForm(FlaskForm):
    breed=StringField('What breed are you?',validators=[DataRequired()])
    neutered=BooleanField("Have you been neutered?")
    mood=RadioField("Please choose your mood:",choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choices=SelectField(u'Pick your favorite food:',choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
    feedback=TextAreaField()
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form =InfoForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        session['neutered']=form.neutered.data
        session['mood']=form.mood.data
        session['food_choices']=form.food_choices.data
        session['feedback']=form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template('2.index.html',form=form)

@app.route('/thankyou',methods=['GET','POST'])
def thankyou():
    return render_template('2.thankyou.html')

if __name__=='__main__':
    app.run(debug=True)