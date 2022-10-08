import os, requests, json, time
os.system("clear")

url = "https://www.dailymotion.com/video/x7w349h"

def download_data(url):
    p1 = "https://api.w03.savethevideo.com/tasks"

    obj = {"type":"info","url": url }

    r = requests.post(p1, json = obj)
    h = json.loads(r.text)['href']

    print(h)

    g1 = "https://api.w03.savethevideo.com//" + h
    time.sleep(3)
    r2 = requests.get(g1)

    jr2 = json.loads(r2.text)

    #print(jr2)
    print(jr2['result']['title'])
    print(jr2['result']['url'])

    return_data = {
        "title" : jr2['result']['title'],
        "url" : jr2['result']['url']    
    }

download_data(url)