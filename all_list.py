import os, json
os.system("clear")

load_data = open("playlist.json")

jj = json.load(load_data)

aa = jj['result']['entries']

nn = []
for a in aa:
    nn.append(a['url'])

#print(nn)

from fetch import download_data
for n in nn[:5]:
    print(n)
    download_data(n)

