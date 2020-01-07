import requests
print(requests.__version__)
var = requests.get("https://github.com/KaixiangCS/Cmput-404-Lab1/blob/master/script.py")
print(var.content)
