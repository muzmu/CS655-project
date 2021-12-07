import requests

proxy={"http": "10.10.1.2:8080"}
url = 'http://ipv4.download.thinkbroadband.com/20MB.zip'
print("Downoading object without Cache")
b = requests.get(url)
print("Object Downloaded")
print("Time (s) taken to download", b.elapsed.total_seconds())
print("Throughput" , len(b.content)/b.elapsed.total_seconds())
print("----------------------------------------")
print("Downoading object with Cache First Time")
b = requests.get(url, proxies=proxy)
print("Object Downloaded")
print("Time (s) taken to download", b.elapsed.total_seconds())
print("Throughput" , len(b.content)/b.elapsed.total_seconds())
print("----------------------------------------")
print("Downoading object with Cache Second Time")
b = requests.get(url, proxies=proxy)
print("Object Downloaded")
print("Time (s) taken to download", b.elapsed.total_seconds())
print("Throughput" , len(b.content)/b.elapsed.total_seconds())
print("----------------------------------------")
