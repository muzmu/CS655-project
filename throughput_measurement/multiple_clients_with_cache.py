import requests
import _thread
from multiprocessing import Process, Queue
import time
proxy={"http": "10.10.1.2:8080"}

size = 10
#url = 'http://ipv4.download.thinkbroadband.com/20MB.zip'
url = 'http://ipv4.download.thinkbroadband.com/'+str(size)+'MB.zip'
#url = 'http://speedtest.tele2.net/'

def download_without_cache(url,i):
    print(i,"Downoading "+str(size) + "MB object without Cache")
    start=time.clock()
    b = requests.get(url)
    stop = time.clock() - start
    print(i,"Object Downloaded")
    print(i, "Time (s) taken to download",stop)
    print(i, "Throughput" , len(b.content)/stop)
    print(i, "----------------------------------------")

def download_with_cache_first(url,proxy):
    print("Downoading "+str(size) + "MB object with Cache First Time")
    start=time.clock()
    b = requests.get(url, proxies=proxy)
    stop = time.clock() - start
    print("Object Downloaded")
    print("Time (s) taken to download", stop)
    print("Throughput" , len(b.content)/stop)
    print("----------------------------------------")

def download_with_cached_file(url,proxy,i):
    print(i,"Downoading "+str(size) + "MB object with Cache")
    start=time.clock()
    b = requests.get(url, proxies=proxy)
    stop = time.clock() - start
    print(i,"Object Downloaded")
    print("Time (s) taken to download", stop)
    print(i,"Throughput" , len(b.content)/stop)
    print(i,"----------------------------------------")
download_with_cache_first(url,proxy)

for i in range(1,11):
    _thread.start_new_thread(download_with_cached_file, (url,proxy,i))
    #p=Process(target=download_with_cached_file,args=(url,proxy,i))
    #p.start()

print("Started all 10 threads") 
while True:
    try:
        pass
    except KeyboardInterrupt:
        exit()
