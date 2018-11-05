import urllib2
from bs4 import BeautifulSoup
from time import sleep
import re

# ambil url
detik = 'https://www.detik.com'
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36' }
req = urllib2.Request(detik, None, headers)
dres = urllib2.urlopen(req)
dhtml = dres.read()
dsoup = BeautifulSoup(dhtml)
list01 = [el["href"] for el in dsoup.findAll("a", href=re.compile("d\-\d+"))]
seen = set()
dlist01 = [x for x in list01 if x not in seen and not seen.add(x)]
dlist = [x for x in dlist01 if x not in dlistOld]

x=[]
for url in dlist:
    res = urllib2.urlopen(url)
    x.append(res.read())
    dlistOld.append(url)
    # di production ada baiknya kita masukkan sleep untuk mengurangi waktu unduh
    #sleep(20)

# lawas sengaja ga dibuang dul !
y=[]
for html in x:
    soup = BeautifulSoup(html)
    if len(soup.select("div[class=detail_text]")) == 0 :
        continue
    elif soup.find('div',{'class':'jdl'}) is None :
        continue
    else :
        # selector untuk detik 
        [s.extract() for s in soup.select("div[class=detail_text]")[0].findAll('script')]
        y.append(soup.select("div[class=detail_text]")[0].text.strip('\n').replace('\n',' ').replace('\t',''))

## testing
for html in x:
    soup = BeautifulSoup(html)
    if len(soup.select("div[class=detail_text]")) == 0 :
        continue
    elif soup.find('div',{'class':'jdl'}) is None :
        continue
    elif soup.find('div',{'class':'jdl'}).find('span',{'class':'date'}) is None :
        soup.find('div',{'class':'jdl'}).find('div',{'class':'date'}).text.lower().replace(',','').split()
        soup.select("div[class=detail_text]")[0].findAll('div',{'class':'lihatjg'})
        soup.findAll('img')[11].get('src')
    else :
        soup.find('div',{'class':'jdl'}).find('span',{'class':'date'}).text.lower().replace(',','').split()
        soup.select("div[class=detail_text]")[0].findAll('div',{'class':'lihatjg'})
        soup.findAll('img')[11].get('src')

xx=[]
tag = re.compile('(?:.(?!\())+$')
for html in x:
    soup = BeautifulSoup(html)
    z={}
    try:
        z['judul']=soup.find('div',{'class':'jdl'}).find('h1').text
        z['date']=soup.find('div',{'class':'jdl'}).find('div',{'class':'date'}).text.lower().replace(',','')
        [s.extract() for s in soup.select("div[class=detail_text]")[0].findAll('script')]
        isi=soup.select("div[class=detail_text]")[0].text.strip('\n').replace('\n',' ').replace('\t','')
        z['lokasi']=isi.split('- ')[0]
        z['konten']=tag.split(isi.split('- ')[1])[0]
        z['attr']=tag.split(isi.split('- ')[1])[1]    
    except:
        continue
    xx.append(z)


# tag
#re.findall(r'(?:.(?!\())+$', i)
# foto
#re.findall(r'(\(Foto:.*?\))',y[28])
# url foto
#soup8.findAll('img')[11].get('src')
# artikel terkait detik
#soup.select("div[class=detail_text]")[0].findAll('div',{'class':'lihatjg'})
