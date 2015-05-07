import scrapy
from project1.items import Project1Item

base_coe_url = "https://wcd.coe.int"

class CoeSpider(scrapy.Spider):
    name = "coe"
    allowed_domains = ["coe.int"]

    def start_requests(self):
        # Pagination = 999999 (all results in one page)
        # BeginDate, EndDate filter results by date.
        return [scrapy.FormRequest("https://wcd.coe.int/search.jsp?&Pagination=999999&ShowBanner=no&ShowNavBar=both&Site=CM%20&BackColorIntranet=EDB021&BackColorInternet=C3C3C3&BackColorLogged=F5D383&ShowRes=yes&DocType=docDecision&FilingPlan=fplCM_VolDecisions&Language=lanEnglish&Sector=secCM&ShowCrit=top&ShowPeriodBox=dates&ShowPaginationBox=no&ShowFullTextSearch=yes&ShowDocTypeBox=no&ShowEntityBox=no&ShowEventBox=no&ShowGeoBox=no&ShowLanguageBox=no%20&ShowThemeBox=no&ShowSectorBox=no&ShowSectorLevelBox=no&ShowFileRefBox=no&ShowKeywordBox=no&ResultTitle=Compilation%20of%20decisions%20by%20meeting&CritTitle=Compilation%20of%20decisions%20by%20meeting&Lang=en",
                                     formdata={'BeginDate':'1980','EndDate':'2015'},
                                     callback=self.parse_main_page)]
    def parse_main_page(self,response):
            result = []
            for data in response.xpath("//*[@class='paddingLR25px']/a/@href").extract():
                result.append(scrapy.Request(base_coe_url + data,callback=self.parse_document_page))
            return result

    def parse_document_page(self,response):
            result = []
            if 'Open Word version' in response.body:
                url = base_coe_url + response.xpath("//a[contains(@title,'Open Word version')]/@href")[0].extract()
            elif 'Open PDF version' in response.body:
                url = base_coe_url + response.xpath("//a[contains(@title,'Open PDF version')]/@href")[0].extract()
            else:
                # Hay documentos que no tienen link ni de word ni de pdf
                print '\n\n\n\n\n' + response.url + '\n\n\n\n\n'
            try: 
                item = Project1Item()
                filename = response.xpath('//p[@class="CM_Title"]/b/text()').extract()[0]
                item['file_urls'] = {'file_url':url,'file_name': filename}
                result.append(item)
            except:
                pass
            return result
