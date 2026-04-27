from flask import jsonify
from dao.models import ScanTask, ScanResult
from dao.db import db
from core.algorithm import SensitiveDetector

detector = SensitiveDetector()


class ScanService:
    def scan_file(self, file):
        # 1. 校验文件
        if not file.filename.endswith(".py"):
            return jsonify({"code": 400, "msg": "仅支持上传.py文件"})

        # 2. 读取并检测
        content = file.read().decode("utf-8")
        vuln_list = detector.detect(content)

        # 3. 存入数据库
        task = ScanTask(filename=file.filename, vuln_count=len(vuln_list))
        db.session.add(task)
        db.session.flush()

        for vuln in vuln_list:
            result = ScanResult(
                task_id=task.id,
                line_num=vuln["line_num"],
                risk_level=vuln["risk_level"],
                content=vuln["content"],
                suggestion=vuln["suggestion"]
            )
            db.session.add(result)
        db.session.commit()

        return jsonify({
            "code": 200,
            "msg": "扫描完成",
            "vuln_count": len(vuln_list),
            "data": vuln_list
        })