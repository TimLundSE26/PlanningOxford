import re
import scraperwiki
import requests
from lxml.html.soupparser import fromstring
from time import sleep

month = "Oct 17"
laurlroot = "http://planning.lewisham.gov.uk"

def search(mth):
  	request_data = {"month": mth, "dateType": "DC_Validated" , "searchType": "Application" }
	
	sleep(2)
	result = requests.post('http://planning.lewisham.gov.uk/online-applications/monthlyListResults.do?action=firstPage', request_data)
	
	if not result:
		print "No result returned"
		return
	
	result_dom = fromstring(result.content)  
  	applications = result_dom.xpath("//li[@class='searchresult']")
  	print len(applications)	
	
	for application in applications:
		link = "".join(application.xpath('a/@href')).strip()
		description = "".join(application.xpath('a/text()')).strip()
		address = "".join(application.xpath('p[@class="address"]/text()')).strip()
		meta = "".join(application.xpath('p[@class="metaInfo"]/text()')).strip()	
		print link, address
	


print "Starting run"

search(month)
