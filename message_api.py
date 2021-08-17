from message_models import app,db,Admin,User,Tag,Message

@app.route("/index")
def hello_world():
    return 'hello world'
# 管理员初始化

# 管理员登陆

# 管理员退出登录

# 管理员增标签

# 管理员删标签

# 管理员删留言


# 用户初始化

# 用户登录

# 用户退出登录

# 用户发布留言

# 用户删除留言

# 用户查看留言记录
if __name__ == '__main__':
    app.run()