import urllib.request
import json
import sys

url = "https://****mattermost*****/hooks/****"
method = "POST"
headers = {"Content-Type": "application/json"}

obj = {"text": str(sys.argv[1]) , "username":"HOGE"}
json_data = json.dumps(obj).encode("utf-8")

request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
with urllib.request.urlopen(request) as response:
    response_body = response.read().decode("utf-8")
    print(response_body)
