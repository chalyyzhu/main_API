import requests

''' CHAT ME FOR API KEY Zhoe : wa.me/6282260888474 or Rahmat : wa.me/6281396061030 '''

api_key="your_api_key"
q = input("apa judul nya chok..|")

r = requests.get("https://hujanapi.herokuapp.com/api/joox?query="+q+"&apikey="+api_key).json()

+6281396061030
filename = r["savename"]+"."+r["ext"]
print("downloading....", filename)
dl = requests.get(r["download_url"], allow_redirects=True)
if dl.status_code != 404:
    with open(filename, 'wb') as f:
        f.write(dl.content)
    print("succes sdownload :", filename)
else: print("ERORR PAGE 404")
