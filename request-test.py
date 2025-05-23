import requests

access_token = "ca75ed81bf45d40dd75f29f5ab49f88d9ad7522081ead947a2ea7ac08e34"
url = "https://api.telegra.ph/getAccountInfo"
params = {
    "access_token": access_token
}
response = requests.get(url, params=params)
print(response.json())
