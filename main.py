import requests

response = requests.get("https://www.codeforlife.education/")
assert response.ok
