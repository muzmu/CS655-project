import wget

url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'

file = wget.download(url)

print(file)

