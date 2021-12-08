Install Instructions:
Please Install the cache using rsppec and then place the configuration files in /opt/ats/etc/trafficserver/ directory for quich Forward proxy setup. The Tested configuyrations are given in the bottom of this file.


Web Caching

Muzammil Hussain,

Github link : [https://github.com/muzmu/CS655-project.git]()

GENI Slice : mini-project-muz

**Introduction**

 web cache is a proxy server which can caches the objects both on client side as well as server side. These objects can be images, audio files, videos or any kind of documents. This caching can help in reducing the delay while browsing the web. Moreover, by caching the objects inside the organization’s network or a NAT you can potentially reduce the traffic which goes out of the organization and reduce the cost drastically. In this project we are going to implement a Forward proxy in the Transparent manner. All the user requests will go to this transparent proxy which will analyze the request if the requested object is in the cache, then the object will be served to the client after checking the validity of the object. If the object is not in the cache the proxy server will request the object from the server forward the object back to user and cache the object for future. At the end of this project, we will know how a transparent forward proxy server is set up. How the client requests are directed to a proxy server, what are the different configuration available for setting up a web cache using a proxy server, what is the impact of a cache on the Throughput and Download time of an object. And what is the impact of different Configurations of the Cache on the Throughput and Download time.

**Experimental Methodology**

1. **Apache Traffic Server**

We are using Apache Traffic Server (ATS) as a transparent forward proxy which will get all the requests from the clients and check if the requested object is in the cache or not. If the requested object is not in the cache, it will request the object from the origin server and forward the object to the user while keeping a copy of the object in the cache in case if some user asks for the same object again. Transparent proxies are usually deployed in a way that no user configuration is needed i.e., a user has no choice if the request goes to the proxy or not. It is usually implemented at the gateways of the organizations or origin servers and all the requests are routed to the proxy by the routing tables and the routers. But for our project because we cannot change the routing mechanisms on GENIE, we are going to send the request to the proxy my specifying the proxy address and the proxy will treat the request as a regular user request. 

1. Setup and Methodology 1.

Initially we implemented a topology on GENI in a way that had 10 user nodes and a caching node. All the user nodes will mimic a normal user and send web requests to the caching node. Caching node will run ATS and get all the requests form users and serve them object from the cache or request from origin server and store it in the cache if the object is already not in the cache. The entire topology will work like a subnet when the cache is used. After implementing the TAS and the user nodes when we started taking the measurements, we found out that the proxy was working perfectly fine if you send the requests to the proxy one user at a time. If a new object was requested the first request would take a lot of time but the subsequent requests would take significant less time compared to the first request. But if all the nodes request the object at the same time from the cache it would take more time to fetch the object from the cache, then to fetch it from the origin server. We thought it was an issue with the configuration of the ATS which was not handling parallel requests. We went through almost all the configuration options but still the issue was there. After a lot of time when we looked at the total number of cores of the GENI node we realized that there was only one core available for the node and that was the bottleneck because one core could not serve to all the nodes at the same time. We tried to register more resources with more cores, but we were not able to register any resources with more than one core. We also tried request smaller objects from the cache, but it was really hard to run request commands from 10 different machines at the same time especially when the requested object is fetched in under a second. If you try to increase the size so the command runs a little longer then the same issue of cache server overloading occurs. Then we considered to redesign our topology to still show the effectiveness of the cache buying only two nodes but multiple threads. The topology is shown below.


1. Set up and Methodology 2

This time we implemented a topology on GENIE with only two nodes one cache server and one user node, but the user node will act as multiple users by sending requests through different threads. The cache proxy will be the same as before the only thing is now all the requests will go through the proxy unlike the previous method where only the requests which were meant to go to cache would go to the cache proxy. We can disable the proxy and it will act as a relay and not cache object but the cup limitation will be on both kind of requests(Cache requests and non-cache requests) because all the requests will go to same proxy the only difference being the when the Cache is enabled it will cache objects or serve from the cache but when the cache is disabled it will not server the requests from the cache and it will always request objects from the origin server. This method turned out to be exactly how the transparent proxies in real world work the only difference being the caching is disabled only for specific domains, but we had to completely disable the cache to take measurements for the same domain. Also, this way you can measure how much traffic goes out of the organization in our case how much traffic leave the cache proxy and get served by the origin server. The topology of genie is given below.

1. Analysis Scripts
1. For the measurement of throughput and Download time and the impact of different network conditions and Object Size we used python requests library which crafts a request and send it to the proxy server. We found a website that has different size of objects just to download for testing and we used that website for our testing. For network conditions and no cache requests we relied on the proxy configurations and had to change them to get the measurements. The details of all the steps to run the script and re-produce the results will be given in user Instructions section. 

Results

User Instructions:

1. Running without Cache:

Log into the node-0 of Method 2 topology. In the Throughput measurement folder there are 4 files. To run the test serially run ***python3  multiple\_clients\_without\_cache\_cerial.py***  it will request a 100MB object 10 times from a server and give you the download time (s) and the Throughput (Bytes). You can change the object size in the object variable inside the file the supported object sizes are 5,10,20,50,100,200 and 500. I tested with all of them the influence of the cache is more clear while downloading object >50MB but you will have to allow caching of bigger objects in the Cache side.

1. Running with Cache:

Log into the cache node. open /opt/ats/etc/traficserver/records.config make sure the variable 

*proxy.config.http.cache.http* is set to 1. Now go to node-0 and run the scripts with the cache. As I mentioned in the methodology you might have to limit the network speed for the cache to see the clear difference between caching and non-caching because the bottleneck is the CPU. Recommended limit Object size 20MB and Speed limit 5000000. Use the following command on cache to limit the network speed *sudo wondershaper eth0 5000000 5000000*

1. Cache server: 

**Start** : sudo /opt/ats/bin/trafficserver start RUN this commands twice

**Stop** : sudo /opt/ats/bin/trafficserver stop 

**Reload Configuration** : sudo /opt/ats/bin/traffic\_ctl config reload

**Clear all Cache**: sudo /opt/ats/bin/traffic\_server -Cclear

**Analysis**

I tested the Cache proxy with multiple Paraments, Cache Eviction Policy, max-age of the object, Different Network Speeds. Different number of clients, Serial and Parallel Requests, Size of the object to be cached, Changing the size of the memory cache and changing size of Storage Cache. 

**Effect of Cache Eviction Policy and max-age:**  

The effect if Cache eviction Policy and max-age of the object in the cache is almost the same. Both affect the subsequent requests. You can change the cache eviction policy by changing the variable *proxy.config.cache.ram\_cache.algorithm* in cache.config and you can change the max-age of an object by changing the variable *ttl-in-cache* or *pin-in-cache.* Both Eviction policy and the max-age Affect only one subsequent request if the object is evicted because max age expired, or it was removed by eviction algorithm. But once the object is requested again the cache stores it again and the subsequent requests are not affected by these variable until it is evicted again.



In the first graph the max age is 7sec but the age is not renewed when the object is fetched again. So after 7 sec object is evicted because of max-age expiration. Every odd request is a miss because the object is not in the cache and every even request is a hit because object is in the cache. Each request is made after 7 seconds. For the second graph each subsequent renewes the max-age of the object so it does not expire. 

**Effect of Number of Client and Network Speed:** 

As I mentioned in the methodology section the limit was that we had only one core for the cache server, so it was really hard to get the result of the cache with multiple users accessing the cache at the same time. I first thought of implementing Multiple cache servers and having a load balancer to redirect the requests. But that was way out of scope for the Project. I settled on limiting the network speed such that the speed becomes bottleneck over CPU. I kept the speed inside the subnet the same because in real world you have more bandwidth inside the subnet compared to outside bandwidth. This Configuration also allowed me to see the benefit of having a proxy because most of the traffic will not leave your subnet if the object is already Cached. I mimicked multiple clients by having different threads and limited the network on cache side using ***wondershaper***. The results are shown in the graph below. I have added the Screen shots of the results on github with the description as the file name. You can see all the scrren shots of the results there. 



You can see from the graphs the benefit of having the cache. When the cache is not used it takes much longer to get an object. Also you can see the diffence between two graphs when there is no bandwidth limit on the outside networks vs when there is a litmit on the network. Cache is particularly helpful you’re your speed inside the local Network is way fater then the external network. Screen shots of all these runs are availeble on the github repo.

Effect of Cached Object Size and Size limit for RAM objects:

After finihshing the main goal of testing the affect of cache overall I also Tested different Other papramters such as changing the object size which can be kept in the RAM. You can change that in the cache.config file by changing the varible max\_size.object\_in\_ram The default was 4MB. I cahnged it to 100MB and this increased the throughput. But the affect was very little because the bottleneck was CPU. I also experimented with what object size to store in the cache. The default in cache.stroage was 10MB. If you change it to higher values you can cache bigger objects. If you want to download a file bigger that 100MB please go to cache.storage and change the object size so it can cache bigger objects. Apart from all that I also experimented with mutiple other configurations all the configurations will be given in the github repo and I can not put them here because of the page limit on final report. If you are interested please go to github repo and see which configurations I tested. 


Conclusion:

In this project I implemented a web-cache that caches objects when they are requested by the useres and served from the cache on future requests. This way it reduces the ftech time of objects and prevent leaving the trafic from the orgnizational network helping in reducing the cost. I used ATS to implemet the Cache proxy and anothre GENI node to act as multiple clients by using different threads in python script. Even tho the Cache proxy was the bottlenck because of only one CPU available to it I was still able to show the benefits of having a web-Cache by making the External network a bottlenck over CPU. I also studied multiple paraments inside the webcahce such as Eviction policy, Affect of keeping objects in RAM cache, Affect of Caching bigger objects, Chaning the max-life of an object in the cache. Because if the CPU bottleneck I faced a lot of isssues in measuring the impact of these parameters in the Cache becaue CPU time was dominating everything. I was still able to see the affect for many of the Parameters. 

Division of Labor:

Muzammil Hussain: I did everything alone. All the proxy set up measurement scripts and the entire writeup. Please Email other two people and ask them what they did. I will be okay if you will mark them based on this report and project. But I would like to be evaluated alone. I would request you to be lenient with other team members because these are stressful times but I cannot afford to lose marks just because they did not contribute, as I spent so much time dealing with all the issues alone and doing everything without any support in the middle of all my other projects and assignment. 



Tested Configuration Variables while figuring out the slowness of the cache server and for measuremnts:
CONFIG proxy.config.url_remap.remap_required INT 0
CONFIG proxy.config.reverse_proxy.enabled INT 0
dest_domain=example.com suffix=js action=never-cache
dest_domain=example.com ttl-in-cache=1d
proxy.config.exec_thread.limit
proxy.config.accept_threads
proxy.config.restart.active_client_threshold
proxy.config.net.connections_throttle
proxy.config.net.max_connections_in
proxy.config.net.max_requests_in
proxy.config.net.throttle_delay
proxy.config.http.flow_control.enabled
proxy.config.http.websocket.max_number_of_connections
proxy.config.cache.enable_read_while_writer
proxy.config.http.cache.http
proxy.config.http.cache.ignore_client_no_cache
proxy.config.http.cache.ignore_server_no_cache
proxy.config.http.cache.required_headers
proxy.config.http.cache.guaranteed_min_lifetime
proxy.config.http.cache.guaranteed_max_lifetime
proxy.config.http.cache.ignore_client_cc_max_age
proxy.config.cache.min_average_object_size
proxy.config.cache.permit.pinning
proxy.config.cache.ram_cache.size
proxy.config.cache.ram_cache_cutoff
proxy.config.cache.ram_cache.algorithm
proxy.config.http.cache.heuristic_min_lifetime
proxy.config.body_factory.enable_logging


