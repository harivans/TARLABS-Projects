import requests
from lxml import  html


headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'en-US,en;q=0.5',
           'Connection' : 'keep-alive',
           'Cookie':'JSESSIONID=DDF88C31E5F67045AEE8AD3388AA4FAB.server240; SERVERIDN=CC; hscPopup7=yes; __gads=ID=aaf763c3ba9e226c:T=1442210390:S=ALNI_MZY6hSIKkvWBBYkYJpkz8RR_U9tPw; __uzma=ma79db7d2f-8128-4ca3-8ad8-9ad7a350efaf9823; __uzmb=1442210390; __uzmc=729314070549; __uzmd=1442211635; __atuvc=3%7C37; _ga=GA1.2.2107601816.1442210390; __utma=185401775.2107601816.1442210390.1442210393.1442210393.1; __utmc=185401775; __utmz=185401775.1442210393.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); faceBookPopup=faceBookPopup',
           'Host': 'www.cardekho.com',
           'Referer':'http://www.cardekho.com/',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'
           }

url = 'http://www.cardekho.com/ajaxCallAction.do'
req = requests.post(url=url,headers = headers)
print req
res = html.fromstring(req.text)
print res
data = res.xpath("//select[@id='usedCarCitySelectByBudget']/option[position()>2]/@value")
print data


