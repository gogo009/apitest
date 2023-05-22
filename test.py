import requests

session = requests.session()

# url = "http://newoa.800best.com"
url = "http://oa.800best.life/best/oa"

headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://oa.800best.life", "Content-Type": "application/x-www-form-urlencoded"}

data = {"username": "best_oa", "password": "Abc2467#123"}

req = session.post(url, headers=headers, data=data)

print(req.content)
