import requests

# 发送请求以创建帐户
response = requests.get("https://api.telegra.ph/createAccount", params={
    "short_name": "tyh",
    "author_name": "tyh"
    # "author_url": "https://example.com",  # 如果有可以添加
})

# 检查响应状态
if response.ok:
    data = response.json()
    if data['ok']:
        access_token = data['result']['access_token']
        print("Access Token:", access_token)
    else:
        print("Error:", data['error'])
else:
    print("Failed to reach Telegraph API")
