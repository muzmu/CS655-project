import requests

proxy={"http": "10.10.1.2:8080"}
url = 'http://ipv4.download.thinkbroadband.com/20MB.zip'

a = requests.get(url, proxies=proxy)

#open('1.mp3','wb').write(a.content)
print(a.elapsed)
print(len(a.content)/a.elapsed.total_seconds())
a = requests.get(url, proxies=proxy)
print(a.elapsed)
print(len(a.content)/a.elapsed.total_seconds())
b = requests.get(url)
print(b.elapsed)
print(len(b.content)/b.elapsed.total_seconds())
