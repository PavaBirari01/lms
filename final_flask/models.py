# from codejana_flask.__init__ import db
from flask import redirect, url_for
from flask_login import UserMixin
from final_flask import db,login_manager
from datetime import datetime
from flask import redirect, url_for 
@login_manager.user_loader
def load_user(user_id):
    return Datas.query.get(user_id)

@login_manager.unauthorized_handler
def unautheorized():
    return redirect(url_for('register'))

    
class Datas(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    # image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

class Subjects(db.Model,UserMixin):
    subname=db.Column(db.String(20),unique=True,nullable=False)
    subid=db.Column(db.Integer,unique=True,nullable=False,primary_key=True)

class Savebooks(db.Model,UserMixin):
    booktitle=db.Column(db.String,unique=True,nullable=False)
    bookNumber=db.Column(db.Integer,unique=True,nullable=False,primary_key=True)
    subjectId=db.Column(db.Integer,unique=True,nullable=False,primary_key=True)
    bookAuthor=db.Column(db.String,nullable=False)
    PublisherName=db.Column(db.String,nullable=False)
    price=db.Column(db.Integer,unique=True,nullable=False,primary_key=True)
    pages=db.Column(db.Integer,unique=True,nullable=False,primary_key=True)

# results = db.session.query(Datas,Subjects).join(Subjects).all()
    
# for datas,subjects in results:
#     print(datas.username,subjects.booktitle)
    # def __repr_(self):
    #     return f'{self.username} : {self.email} : {self.date_created.strftime("%d/%m/%y, %H:%M:%S")}'