import jwt
import time
from config import Config

# 生成Token
def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": time.time() + Config.JWT_EXPIRE
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

# 校验Token
def verify_token(token):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except:
        return None