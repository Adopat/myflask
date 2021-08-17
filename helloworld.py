from flask import Flask, request, jsonify, session

#实例化Flask 对象 __name__ 指的时在此文件运行
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key ="asdasdsdkkk"
@app.route("/")
def hello_world():
    return "hello world!"
@app.route("/hey/<username>")
def hey_name(username):
    return "hey %s"%(username + username)
@app.route("/my/<int:number>")
def my_number(number):
    return "my %s"%(number + number)
@app.route("/baidu")
def baidu():
    return redirect("https://www.baidu.com")
@app.route("/bilibi")
def bilibili():
    return redirect("https://www.bilibili.com/")
@app.route("/test/my/first",methods=['post',"GET"])
def first_post():
    try:
        #请求post
        my_json = request.get_json()
        print(my_json)
        get_name = my_json.get("name")
        get_age = my_json.get("age")
        if not all([get_name,get_age]):
            return jsonify(msg='缺少参数')
        get_age +=10
        #返回 json 数据
        return jsonify(name=get_name,age=get_age)
    except Exception as e:
        print(e)
        return jsonify(msg="出错了哦，请查看是否正确访问！！")
# 登录
@app.route("/try/login",methods=["POST"])
def login():
    """
    账号 username asd123
    密码 password asdasd
    :return:
    """
    get_data = request.get_json()
    username = get_data.get("username")
    password = get_data.get("password")
    if not all([username , password]):
        return jsonify(msg="参数不完整")
    if username =="asd123" and password == "asdasd":
        # 如果验证通过 保存登录状态到 session 中
        session["username"] = username
        return jsonify(msg="登录成功！！")
    else:
        return jsonify(msg="账号或密码错误！！")
# 检查登录状态
@app.route("/session",methods=["GET"])
def check_session():
    username = session.get("username")
    if username is not None:
        return jsonify(username=username)
    else:
        return jsonify(msg="出错了，没登陆")
# 登出
@app.route("/try/logout",methods=["GET"])
def logout():
    session.clear()
    return jsonify(msg="退出登录成功！！")
app.run()