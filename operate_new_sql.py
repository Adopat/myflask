from learn_sql import db,Student,Grade

# 增
s = Student(name='张三',gender='男',phone='12345678900')
s1 = Student(name='张蛋',gender='男',phone='12345678901')
s2 = Student(name='李四',gender='男',phone='12345678902')
s3 = Student(name='李鬼',gender='男',phone='12345678903')
s4 = Student(name='王五',gender='女',phone='12345678904')

# 添加语句
# 逐条添加
# db.session.add(s4)
# db.session.commit()
# 一次性添加
# db.session.add_all([ s,s1 , s2 , s3 , s4])
# db.session.commit()

# 查单一的数据
# stu = Student.query.get(2)
# print(stu.name)
# print(stu.gender)
# print(stu.phone)

# 查找全部数据
# stu = Student.query.all()
# for i in stu:
#     print(i.name,i.gender,i.phone)

# 按照条件来查询 filter()
# stu = Student.query.filter(Student.gender =='女')
# for i in stu:
#     print(i.name,i.gender,i.phone)

# 类似SQL 的查询方法
# stu = Student.query.filter_by(name='王五').all()
# for i in stu:
#     print(i.name,i.gender,i.phone)

# 改
# stu = Student.query.filter(Student.name=='张三')
# for i in stu:
#     print(i.name,i.gender,i.phone)
# 第一种改法
# stu = Student.query.filter(Student.name=='张三').update({'name':'张一'})
# db.session.commit()
# stu1 = Student.query.filter_by(name='张一').all()
# for i in stu1:
#     print(i.name,i.gender,i.phone)
# stu2 = Student.query.all()
# for j in stu2:
#     print(j.name,j.gender,j.phone)
# 第二种

# stu = Student.query.filter(Student.gender=='男').first()
# stu.gender = '女'
# db.session.add(stu)
# db.session.commit()
#
# stu = Student.query.all()
# for i in stu:
#     print(i.name,i.gender,i.phone)


# 将所有的男的改为女的
# stu = Student.query.filter(Student.gender=='男').update({'gender':'女'})
# db.session.commit()
# stu = Student.query.all()
# for i in stu:
#     print(i.name,i.gender,i.phone)

# 将所有女的改为男的 第二种方法
# stu = Student.query.filter(Student.gender=='女').all()
# for i in stu:
#     i.gender='男'
#     db.session.add(i)
# db.session.commit()
# stu = Student.query.all()
# for i in stu:
#     print(i.name,i.gender,i.phone)

# 删
# stu = Student(name='赵六',gender='女',phone='12345678905')
# db.session.add(stu)
# db.session.commit()
# stu = Student.query.all()
# for i in stu:
#     print(i.name,i.gender,i.phone)
# stu = Student.query.filter(Student.name=='赵六').update({'gender':'男'})
# db.session.commit()
# stu = Student.query.all()
# for i in stu:
#     print(i.name,i.gender,i.phone)
# stu = Student.query.filter(Student.name=='赵六').delete()
# db.session.commit()
# stu = Student.query.all()
# for i in stu:
#     print(i.name,i.gender,i.phone)

# print('-------------------------------------------------')
# grade1 = Grade(grade=100,student_id=1)
# grade2 = Grade(grade=95,student_id=1)
# db.session.add_all([grade1,grade2])
# db.session.commit()
# grade = Grade.query.all()
# for i in grade:
#     print(i.id,i.grade,i.student_id)
# 通过 一访问多
# stu = Student.query.get(1)
# print(stu)
# for i in stu.grades:
#     print(stu.name,i.grade)
# 通过多访问一
grade = Grade.query.filter(Grade.grade=='100').all()
for i in grade:
    print(i.student.name,i.grade)
