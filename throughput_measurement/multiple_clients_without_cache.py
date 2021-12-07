import requests
import _thread

proxy={"http": "10.10.1.2:8080"}
url = 'http://ipv4.download.thinkbroadband.com/20MB.zip'

def download_without_cache(url,i):
    print("Downoading object without Cache")
    b = requests.get(url)
    print(i,"Object Downloaded")
    print(i, "Time (s) taken to download", b.elapsed.total_seconds())
    print(i, "Throughput" , len(b.content)/b.elapsed.total_seconds())
    print(i, "----------------------------------------")

def download_with_cache_first(url,proxy):
    print("Downoading object with Cache First Time")
    b = requests.get(url, proxies=proxy)
    print("Object Downloaded")
    print("Time (s) taken to download", b.elapsed.total_seconds())
    print("Throughput" , len(b.content)/b.elapsed.total_seconds())
    print("----------------------------------------")

def download_with_cached_file(url,proxy,i):
    print(i,"Downoading object with Cache Second Time")
    b = requests.get(url, proxies=proxy)
    print(i,"Object Downloaded")
    print(i,"Time (s) taken to download", b.elapsed.total_seconds())
    print(i,"Throughput" , len(b.content)/b.elapsed.total_seconds())
    print(i,"----------------------------------------")

for i in range(1,15):
    _thread.start_new_thread(download_without_cache, (url,i))

print("Started all 15 threads") 
while True:
    try:
        pass
    except KeyboardInterrupt:
        exit()
