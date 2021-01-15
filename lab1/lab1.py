import requests

#print(requests.__version__)

#r = requests.get('https://www.google.com')
#print(r)

r = requests.get('https://raw.githubusercontent.com/raysarinas/cmput404/master/lab1/lab1.py')
print(r.text)
