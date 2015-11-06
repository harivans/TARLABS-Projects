from scrapy.spider import Spider
from cardealers.vyprvpnConnection import MyVPN
from cardealers.settings import VPN_setting
import logging.handlers
from cardealers.cities import zigwheel_url_cities
import math
from scrapy import Request


logFormatter = logging.Formatter("%(asctime)s line: %(lineno)d  %(funcName)s  %(message)s  " )
logger = logging.getLogger("boostist")
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)


LOG_FILENAME = 'zigwheels_worker.log'

file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,mode='w',
                                               maxBytes=1024*1024*10,
                                             backupCount=10,
                                               )
file_handler.mode='w'
file_handler.setFormatter(logFormatter)
logger.addHandler(file_handler)

logger.info('hello')


textFile_path = '/home/mukesh/TARLAB/CarDealers/car_dealers/zigwheelsDataFiles'

m = MyVPN(username=VPN_setting['username'],password=VPN_setting['password'])

headers = {
                   'Host': 'www.zigwheels.com',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate',
                   'Host' :'www.zigwheels.com',
                   'Referer' :'http://www.zigwheels.com/2db/get_details_of_seller_2db.php?flag=result',
                   'Content-Type':'application/x-www-form-urlencoded' ,
                   'Cookie': 'agent_env=(null); _ga=GA1.2.2124995098.1441604292; _gat=1; __gads=ID=e1f9c79ede78afa3:T=1441604295:S=ALNI_MZyR9wSQy_aaCxMhHfFCTE30UWZtg; PHPSESSID=4eukj34n0g4lru3b17hm6ptnm2; securimage_code_value=a186dddb325fa844adc7674c5e068d1ede086f2c; mf_967cced2-cfb6-456c-ab66-50cf15417b64=-1; _ibeat_session=wpemnfyodloharen; lead_name=vishal; lead_email=s87g1M%2FGl5zXxNfYpce24Q%3D%3D; lead_mobile=dZiko6eLjmqblg%3D%3D; isCaptchaVerified=yes'

                   }
parameters = {
                      'usedListingId':139013,
                      'email':'vishal@gmail.com',
                      'mobile':'8377917513',
                      'name':'vishal',
                      'securityCode':'3GCA'
                      }
cookies = {'lead_name':'vishal','lead_email':'s87g1M%2FGl5zXxNfYpce24Q%3D%3D','lead_mobile':'dZiko6eLjmqblg%3D%3D'}


class Zigwheels(Spider):
    name = 'zigwheels'
    allowed_domains = ['zigwheels.com']
    
    def switch_ip_server(self):
        m.logout()
        m.disconnect()        
        m.random_server()
        m.login()
        m.connect()
    
    def start_requests(self):
        self.switch_ip_server()
        city_count = 0
        for city in zigwheel_url_cities:
            city_count = city_count + 1
            logger.info('{0} :{1}'.format(city_count,city))
            baseUrl = 'http://www.zigwheels.com/used-car/'+city
            logger.info('{0}'.format(baseUrl))
            yield Request(url = baseUrl,headers=headers,callback=self.get_user_id_urls)
    
    
    def get_users_details(self,response):
        name = response.xpath("//div[@class='iframe_field']/p[2]/text()")
        
        rawname = response.xpath("//div[@class='iframe_field']/p[2]/text()")
        if rawname: 
            namelist = str(rawname[0].encode('ascii','ignore')).split(':')
            name = namelist[1]
            
            try:
                email = response.xpath("//div[@class='iframe_field']/p[3]/a/text()")[0]
            except:
                email = ''
            
            try:
                phonelist = response.xpath("//div[@class='iframe_field']/p[4]/text()")[0].encode('ascii','ignore').split(':')
                phone = phonelist[1]
            except:
                phone = ''
        else:
            try:
                namelist = response.xpath("//body/text()")[0].replace('\r\n','').strip().encode('ascii','ignore').split(':')
                name = namelist[1]
            except:
                name = ''
            
            try:
                emaillist = response.xpath("//body/text()")[1].replace('\r\n','').strip().encode('ascii','ignore').split(':')
                email = emaillist[1]
            except:
                email = ''
            try:
                phonelist = response.xpath("//body/text()")[2].replace('\r\n','').strip().encode('ascii','ignore').split(':')
                phone = phonelist[1]
            except:
                phone = ''
        logger.info('scraped.')
        zigwheelsData = name + ', ' + email + ', ' + phone
        return zigwheelsData
    
    def get_user_id_urls(self,reponse):
        totalCar = reponse.xpath("//div[contains(@class,'pull-left')]/text()").extract()
        totalCar = totalCar[0].replace('\r\n\t','').replace('\t','').strip()
        end = totalCar.index(' Used')
        start = totalCar.index('of ')
        pages = int(totalCar[start+3:end])/10
        totalPage = int(math.ceil(pages))
        logger.info("total page:{}".format(totalPage))
        dealerId_Url = reponse.xpath("//div[@class='uc-featured-img']/a/@href").extract()
        mainUrl =  "http://www.zigwheels.com/2db/get_details_of_seller_2db.php?flag=result"
        logger.info('scraping........')
        for uid in dealerId_Url:
            a = uid[uid.rindex('/')+1:]
            parameters.update( {'usedListingId':a})
            yield Request(url = mainUrl,method='POST',headers=headers,cookies=cookies,meta= parameters,callback=self.get_users_details)
        
    
    