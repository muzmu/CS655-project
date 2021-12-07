import requests
import _thread
from multiprocessing import Process, Queue

proxy={"http": "10.10.1.2:8080"}
#url = 'http://ipv4.download.thinkbroadband.com/20MB.zip'
url = 'http://ipv4.download.thinkbroadband.com/100MB.zip'
def download_without_cache(url,i):
    print(i,"Downoading object without Cache")
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
    print(i,"Downoading object with Cache when the object is in the cache")
    b = requests.get(url, proxies=proxy)
    print(i,"Object Downloaded")
    print(i,"Time (s) taken to download", b.elapsed.total_seconds())
    print(i,"Throughput" , len(b.content)/b.elapsed.total_seconds())
    print(i,"----------------------------------------")
download_with_cache_first(url,proxy)

for i in range(1,2):
    #_thread.start_new_thread(download_with_cached_file, (url,proxy,i))
    p=Process(target=download_with_cached_file,args=(url,proxy,i))
    p.start()

print("Started all 8 threads") 
while True:
    try:
        pass
    except KeyboardInterrupt:
        exit()
