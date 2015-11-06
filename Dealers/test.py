import requests
from lxml import html



headers = {
                   'Host': 'www.zigwheels.com',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate',
                   'Host' :'www.zigwheels.com',
                   'Referer' :'http://www.zigwheels.com/2db/get_details_of_seller_2db.php?flag=result',
                   'Content-Type':'application/x-www-form-urlencoded' ,
                   'Cookie': '__uzmc=966467697391; __uzmd=1441950370; JSESSIONID=C2D6F24214B0585AEA94B59ECC251E16.server240; __uzma=mac126ad45-7732-4e95-a5ac-4a20410511986541; __uzmb=1441949197; __uzmc=247957337776; __uzmd=1441950323; SERVERIDN=CC; __gads=ID=f6b821ec48ad2e00:T=1441949202:S=ALNI_MZEGDYEB80c365mHCa7f8i_nKdymA; _ga=GA1.2.1445191871.1441949202; __utma=185401775.1445191871.1441949202.1441949203.1441949203.1; __utmb=185401775.11.9.1441950236259; __utmc=185401775; __utmz=185401775.1441949203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); hscPopup7=yes; __atuvc=6%7C36; __atuvs=55f266111bd841ae005; historySession=C2D6F24214B0585AEA94B59ECC251E16.server240; _dc_gtm_UA-3882094-17=1; __utmt=1'

                   }

res = requests.get("http://www.cardekho.com/used-cars+in+delhi-ncr",headers = headers)
reshtml = html.fromstring(res.text)
names = reshtml.xpath("http://www.cardekho.com/used-cars+in+india")
print names
