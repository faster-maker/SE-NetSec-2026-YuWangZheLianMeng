from dao.models import User
from dao.db import db
from core.jwt_util import generate_token
from flask import jsonify

class AuthService:
    def login(self, username, password):
        # 校验用户
        user = User.query.filter_by(username=username, password=password).first()
        if not user:
            return jsonify({"code": 400, "msg": "用户名或密码错误"})
        # 生成Token
        token = generate_token(user.id)
        return jsonify({"code": 200, "msg": "登录成功", "token": token})