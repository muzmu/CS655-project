from tcp_latency import measure_latency

print(measure_latency(host='10.10.1.2',port=8080,runs=10))
print(measure_latency(host='http://ipv4.download.thinkbroadband.com',runs=10))


