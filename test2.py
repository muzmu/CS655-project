from urllib import request as urlrequest
import urllib
proxy_host = '10.10.1.2:8080'    # host and port of your proxy
url ='http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'


urlrequest.set_proxy(proxy_host, 'http')

response = urlrequest.urlretrieve(url)
print(response)
