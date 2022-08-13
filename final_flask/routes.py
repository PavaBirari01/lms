from flask import Flask, render_template, url_for,redirect,flash,request
from final_flask import forms,app,db,bcrypt,conn
from final_flask.forms import RegistrationForm,LoginForm,ResetRequestForm,AddSubjectForm,AddBookForm
from final_flask.models import Datas,Subjects,Savebooks
# app = Flask(__name__)
from final_flask import app, db
from flask_login import login_required, login_user,logout_user,current_user

@app.route('/')
def homepage():
    return render_template('homepage.html',title='Home Page')

@app.route('/about')
def about():
    return render_template('About.html',title='About')

@app.route('/account')
@login_required
def account():
    return render_template('Account.html',title='Account')

@app.route('/register',methods=['POST','GET'])
def register():
   if current_user.is_authenticated:
    return redirect(url_for('account'))
   form=RegistrationForm()
   if form.validate_on_submit():
    encrypted_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    users=Datas(username=form.username.data,email=form.email.data,password=encrypted_password)
    db.session.add(users)
    db.session.commit()
    flash(f'Account created successfully for {form.username.data}', category='success')
    return redirect(url_for('login'))

   return render_template('register.html',title='Register',form=form)
#    return render_template('register.html",title='Register',form=form)


@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form=LoginForm()
    if form.validate_on_submit():
        user=Datas.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash(f'Login successfully for {form.email.data}',category='success')
            return redirect(url_for('account'))
        else:
            flash(f'Login failed for {form.email.data}',category='danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
#  # main driver function
# if __name__ == '__main__':
#     app.run()

def send_mail():
    pass

@app.route('/reset_password',methods=['GET','POST'])
def reset_request():
    form=ResetRequestForm()
    if form.validate_on_submit():
        user=Datas.query.filter_by(email=form.email.data).first()
        if user:
            send_mail()
            flash('Reset request sent. Check yout mail.','success')
            return redirect(url_for('login'))
    return render_template('reset_request.html',title= 'Reset Request',form=form,legend='Reset Password')

@app.route('/addsubject',methods=['POST','GET'])
def addsubject():
    form=AddSubjectForm()
    if form.validate_on_submit(): 
        users=Subjects(subname=form.subname.data,subid=form.subid.data)
        db.session.add(users)
        db.session.commit()
        flash(f'Account created successfully for {form.subname.data}', category='success')
        return redirect(url_for('account'))
    return render_template('addsubject.html',title='addsubject',form=form)

@app.route('/addbook',methods=['POST','GET'])
def addbooks():
    form=AddBookForm()
    if form.validate_on_submit(): 
        users=Savebooks(booktitle=form.booktitle.data,bookNumber=form.bookNumber.data,subjectId=form.subjectId.data,bookAuthor=form.bookAuthor.data,PublisherName=form.PublisherName.data,price=form.price.data,pages=form.pages.data,)
        db.session.add(users)
        db.session.commit()
        flash(f'Account created successfully for {form.booktitle.data}', category='success')
        return redirect(url_for('account'))
    return render_template('addbook.html',title='addbook',form=form)

@app.route('/libMembersList',methods=['POST','GET'])
def libMembersList():
    if request.method=='POST':
        Member = request.form["Member"]
        cursor = conn.cursor()
        cursor.execute("select * from Datas where username ='"+Member+"'")
        Member = cursor.fetchall()
        print(Member)
        return render_template('libMembersList.html',title='libMembersList',Member=Member)
    else:
        cursor = conn.cursor()
        cursor.execute("select * from Datas")
        Member = cursor.fetchall()
        return render_template('libMembersList.html',title='libMembersList',Member=Member)
        # return render_template('libMembersList.html',title='libMembersList')

@app.route('/booklist',methods=['POST','GET'])
def booklist():
    if request.method=='POST':
        Kitab = request.form["Kitab"]
        cursor = conn.cursor()
        cursor.execute("select * from Savebooks where booktitle ='"+Kitab+"'")
        Kitab = cursor.fetchall()
        print(Kitab)
        return render_template('booklist.html',title='booklist',Kitab=Kitab)
    else:
        cursor = conn.cursor()
        cursor.execute("select * from Savebooks")
        Kitab = cursor.fetchall()
        return render_template('booklist.html',title='booklist',Kitab=Kitab)
    #  return render_template('booklist.html',title='subjectlist')
    

@app.route('/subjectlist',methods=['POST','GET'])
def subjectlist():
    if request.method=='POST':
        SubName = request.form["SubName"]
        SubCode = request.form["SubCode"]
        cursor = conn.cursor()
        cursor.execute("select * from Subjects where subname='"+SubName+"' and subid='"+SubCode+"'")
        Subject = cursor.fetchall()
        print(Subject)
        return render_template('subjectlist.html',title='subjectlist',Subject=Subject)
    else:
        cursor = conn.cursor()
        cursor.execute("select * from Subjects" )
        Subject = cursor.fetchall()
        return render_template('subjectlist.html',title='subjectlist',Subject=Subject)
        


    # form=AddSubjectForm()
    # users=Subjects(subname=form.subname.data,subid=form.subid.data)
    # db.session.add(users)
    # db.session.commit()
   
@app.route('/issuebook',methods=['POST','GET'])
def issuebook():
    return render_template('issuebook.html',title='issuebook')




# @app.route('/showProfiles')
# def Profiles():
#     cursor = conn.cursor()
#     cursor.execute("select * from Datas")
#     Datas = cursor.fetchall()
#     print("Connection established to: ",Datas)
#     return render_template('tables.html',Datas=Datas)