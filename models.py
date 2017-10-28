#encoding:utf-8

from exts import db
from datetime import datetime
#密码加密
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)

    #密码加密
    def __init__(self,*args,**kwargs):
        telephone = kwargs.get('telephone')
        username = kwargs.get('username')
        password = kwargs.get('password')

        self.telephone = telephone
        self.username = username
        self.password = generate_password_hash(password)

    #验证密码的函数
    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return  result

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    #now()获取的是服务器第一次运行的时间
    #now就是每次创建一个模型的时候，都会获取当前的时间
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref=db.backref('questions'))



class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer,db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime,default=datetime.now)

    question = db.relationship('Question',backref=db.backref('answers',order_by=id.desc()))
    author = db.relationship('User',backref=db.backref('answers'))
































