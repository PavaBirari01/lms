from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Length,EqualTo,Email
   
class RegistrationForm(FlaskForm):
    username=StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    email=StringField(label='Email',validators=[DataRequired(),Email()])
    password=PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    confirm_password=PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(label='Sign Up')

class LoginForm(FlaskForm):
    email=StringField(label='Email',validators=[DataRequired(),Email()])
    password=PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    submit=SubmitField(label='Login')
    
class ResetRequestForm(FlaskForm):
    # username = StringField(label='Username',validators=[DataRequired(),Length(min=5,max=20)])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    submit = SubmitField(label='Reset Password' ,validators=[DataRequired()]) 

class AddSubjectForm(FlaskForm):
    subname=StringField(label='Subject Name',validators=[DataRequired()])
    subid=IntegerField(label='Subject Id',validators=[DataRequired()])
    submit=SubmitField(label='Add subject')
    
class AddBookForm(FlaskForm):
    booktitle=StringField(label='Book Title',validators=[DataRequired()])
    bookNumber=IntegerField(label='Book Number',validators=[DataRequired()])
    subjectId=IntegerField(label='Subject ID',validators=[DataRequired()])
    bookAuthor=StringField(label='Book Author',validators=[DataRequired()])
    PublisherName=StringField(label='Book Publisher Name',validators=[DataRequired()])
    price=IntegerField(label='Book Price',validators=[DataRequired()])
    pages=IntegerField(label='Total Pages',validators=[DataRequired()])
    submit=SubmitField(label='Add New Book')