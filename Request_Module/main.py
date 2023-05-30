import requests

url = 'https://github.com/git-for-windows/git/releases/download/v2.40.1.windows.1/Git-2.40.1-64-bit.exe'

r = requests.get(url, stream=True)

split = url.split('/')

name = split[-1]

with open(name, 'wb') as f:
    for i in r.iter_content(chunk_size=1000):
        f.write(i)