from flask import Blueprint, request, jsonify
from dao.models import ScanTask, ScanResult
from utils.auth_decorator import login_required
from service.scan_service import ScanService

scan_bp = Blueprint("scan", __name__, url_prefix="/api/scan")
scan_service = ScanService()

@scan_bp.route("/upload", methods=["POST"])
@login_required
def upload_scan():
    file = request.files.get("file")
    return scan_service.scan_file(file)

@scan_bp.route("/history", methods=["GET"])
@login_required
def get_history():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 10, type=int)

    tasks = ScanTask.query.order_by(ScanTask.create_time.desc()).paginate(page=page, per_page=size)
    data = []
    for task in tasks.items:
        data.append({
            "task_id": task.id,
            "filename": task.filename,
            "vuln_count": task.vuln_count,
            "create_time": str(task.create_time)
        })

    return jsonify({
        "code": 200,
        "data": data,
        "total": tasks.total
    })