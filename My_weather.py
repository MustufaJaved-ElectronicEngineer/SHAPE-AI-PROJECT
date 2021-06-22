import requests
r=requests.get('https://imgs.xkcd.com/comics/python.png')
with open('main.txt','wb') as f:
    f.write(r.content)