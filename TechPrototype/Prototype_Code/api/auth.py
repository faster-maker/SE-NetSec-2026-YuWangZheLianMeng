from flask import Blueprint, request, jsonify
from service.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")
auth_service = AuthService()

@auth_bp.route("/login", methods=["POST"])
def login():
    # 直接读取表单数据
    username = request.form.get("username")
    password = request.form.get("password")
    return auth_service.login(username, password)