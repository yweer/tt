import requests

# API URL
url = "https://alma.fengchiyx.xyz/api/v1/user/checkin"

# 请求头
headers = {
    "authority": "alma.fengchiyx.xyz",
    "method": "POST",
    "path": "/api/v1/user/checkin",
    "scheme": "https",
    "accept": "application/json, application/x-www-form-urlencoded",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTY3LCJzZXNzaW9uIjoiNDIyY2FlY2ViZjM5NjU3NjIyMzVlN2IwZWNhYmFjYzcifQ.YYeqajw9ThD2gSEEfhk0srI6NN3UJKjaBme9rlv67cM",
    "origin": "https://xtyun.top",
    "referer": "https://xtyun.top/",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

# 发送 POST 请求
response = requests.post(url, headers=headers)

# 输出结果
if response.status_code == 200:
    print("签到成功：", response.json())
else:
    print("签到失败，状态码：", response.status_code)
    print("返回内容：", response.text)
