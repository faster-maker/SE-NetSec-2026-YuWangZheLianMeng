from dao.db import db
from datetime import datetime

# 用户表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

# 扫描任务表
class ScanTask(db.Model):
    __tablename__ = "scan_task"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    filename = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, default=datetime.now)
    vuln_count = db.Column(db.Integer, default=0)

# 扫描结果表
class ScanResult(db.Model):
    __tablename__ = "scan_result"
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("scan_task.id"))
    line_num = db.Column(db.Integer)
    risk_level = db.Column(db.String(10))  # 高/中/低
    content = db.Column(db.Text)
    suggestion = db.Column(db.Text)