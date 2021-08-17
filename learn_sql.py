from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+'C:\\myNote\\Flask\\first.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='jjjjkk'
db = SQLAlchemy(app)#实例化的数据库
# 创建学生表
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    gender = db.Column(db.Enum('男','女'),nullable=False)
    phone = db.Column(db.String(11),unique=True,nullable=False)
    grades = db.relationship('Grade',backref = 'student')
# 课程表
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    #teacher_id =
    grades = db.relationship('Grade',backref = 'course')# 课程表关联 成绩表
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher_id')) # 所属教师
# 教师表
class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    gender = db.Column(db.Enum('男','女'),nullable=True)
    phone = db.Column(db.String(11))
    course = db.relationship('Grade',backref='teacher')
# 成绩表
class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer,primary_key=True)
    #course_name =
    grade = db.Column(db.String(3),nullable=False)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))
if __name__ == '__main__':
    db.create_all()
    #db.drop_all()