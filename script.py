import requests
print(requests.__version__)
var = requests.get("hhttps://raw.githubusercontent.com/KaixiangCS/Cmput-404-Lab1/master/script.py")
print(var.content)
