import requests
import threading
import time

# 接口地址
BASE_URL = "http://127.0.0.1:5000/api"
token = ""

# 1. 登录测试
def test_login():
    global token
    res = requests.post(f"{BASE_URL}/auth/login", json={"username":"admin","password":"123456"})
    token = res.json()["token"]
    print("登录测试:", res.json())

# 2. 文件扫描测试
def test_scan():
    files = {"file": open("test.py", "r", encoding="utf-8")}
    headers = {"token": token}
    res = requests.post(f"{BASE_URL}/scan/upload", files=files, headers=headers)
    print("扫描测试:", res.json())

# 3. 并发压力测试（50线程）
def pressure_test():
    threads = []
    for i in range(50):
        t = threading.Thread(target=test_scan)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    test_login()
    test_scan()
    # 压力测试
    # start = time.time()
    # pressure_test()
    # print(f"50并发耗时：{time.time()-start:.2f}s")