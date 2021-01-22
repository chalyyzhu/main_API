import requests

''' CHAT ME FOR API KEY Zhoe : wa.me/6282260888474 or Rahmat : wa.me/6281396061030 '''

api_key="your_api_key"
url = input("url nya chok..|")



r = requests.get("https://hujanapi.herokuapp.com/api/ytdl?url="+url+"&apikey="+api_key).json()["result"]

print("author : {}\ntitle : {}".format(r["author"],r["title"]))
num = input("ketik 1 untuk download music, ketik 2 untuk vidio | ")

if num == "1":
    download = r["mp3"]
    ext = ".mp3"
if num == "2":
    download = r["mp4"]
    ext = ".mp4"

filename = r["title"].replace(" ","_")+ext
print("downloading....  ", r["title"])

dl = requests.get(download, allow_redirects=True)
if dl.status_code != 404:
    with open(filename, 'wb') as f:
        f.write(dl.content)
    print("succes sdownload :", filename)
else: print("ERORR PAGE 404")

