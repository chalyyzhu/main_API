import requests, datetime

''' CHAT ME FOR API KEY Zhoe : wa.me/6282260888474 or Rahmat : wa.me/6281396061030 '''

api_key="apikey lu taro di sini"
url = input("url nya chok..|")

r = requests.get("https://hujanapi.herokuapp.com/api/fbdl?url="+url+"&apikey="+api_key).json()["result"]

num = input("ketik 1 untuk download music,\nketik 2 untuk download vidio hd quality,\nketik 3 untuk download vido Low quality \n==>  ")

if num == "1":
    download = r["audio"]
    ext = ".mp3"
if num == "2":
    download = r["hd"]
    ext = ".mp4"
if num == "3":
    download = r["normal"]
    ext = ".mp4"

basename = "facebook"
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "_".join([basename, suffix])+ext
    
print("downloading....  ", filename)

dl = requests.get(download, allow_redirects=True)
if dl.status_code != 404:
    with open(filename, 'wb') as f:
        f.write(dl.content)
    print("succes sdownload :", filename)
else: print("ERORR PAGE 404")

