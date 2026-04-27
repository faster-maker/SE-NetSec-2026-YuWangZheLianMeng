import ast
import re

# 正则规则
RULES = [
    {"regex": r'password\s*=\s*["\'].*?["\']', "level": "高", "desc": "硬编码密码"},
    {"regex": r'1[3-9]\d{9}', "level": "中", "desc": "手机号泄露"},
    {"regex": r'\d{18}', "level": "中", "desc": "身份证号泄露"}
]

class SensitiveDetector:
    def detect(self, code_content):
        vuln_list = []
        tree = ast.parse(code_content)
        # 遍历AST节点
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                line_num = node.lineno
                code_str = node.value.strip()
                # 正则匹配
                for rule in RULES:
                    if re.search(rule["regex"], code_str):
                        vuln_list.append({
                            "line_num": line_num,
                            "risk_level": rule["level"],
                            "content": code_str,
                            "suggestion": f"请勿硬编码{rule['desc']}"
                        })
        return vuln_list