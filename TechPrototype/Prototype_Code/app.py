from flask import Flask
from flask_cors import CORS
from config import Config
from dao.db import db
from api.auth import auth_bp
from api.scan import scan_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

# 主页 → 测试入口
@app.route("/")
def index():
    return """
    <h1>敏感信息检测系统 - 测试页面</h1>
    <p><a href="/test_login">→ 登录测试</a></p>
    <p><a href="/test_scan">→ 文件上传扫描测试</a></p>
    <p><a href="/test_history">→ 查看扫描历史</a></p>
    """

@app.route("/test_login")
def test_login():
    return open("test_login.html", encoding="utf-8").read()

@app.route("/test_scan")
def test_scan():
    return open("test_scan.html", encoding="utf-8").read()

@app.route("/test_history")
def test_history():
    return open("test_history.html", encoding="utf-8").read()

# 注册接口
app.register_blueprint(auth_bp)
app.register_blueprint(scan_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)