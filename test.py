from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import wget
import requests



html = urlopen("http://web.archive.org/web/20060830152721fw_/http://www.tfmpage.com/cgi-bin/gendb.pl?dbpath=notes&amp;db=chidam")
soup = BeautifulSoup(html.read())
base = "http://web.archive.org"

for a in soup.find_all('a', href=True):
    if ".txt" in a['href']:
        # print(a.text,",","http://web.archive.org"+a['href'])
        r = requests.get("http://web.archive.org"+a['href'])

        with open("notes/"+a.text.replace(" ","_")+".txt", 'wb') as f:
                f.write(r.content)

        # Retrieve HTTP meta-data
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        
        
