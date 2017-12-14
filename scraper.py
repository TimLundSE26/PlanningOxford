# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import re
# import scraperwiki
import requests
# from lxml.html.soupparser import fromstring
from time import sleep

month = "Oct 17"

def search(mth):
#  	request_data = { "searchCriteria.parish": ALL, "searchCriteria.ward": ALL, "month": mth, "dateType": "DC_Validated" , "searchType": "Application" }

  	request_data = {"month": mth, "dateType": "DC_Validated" , "searchType": "Application" }

	# <input type="radio" name="dateType" value="DC_Validated" checked="checked" id="dateValidated">
    
	sleep(2)
	result = requests.post('http://public.oxford.gov.uk/online-applications/search.do?action=monthlyList', request_data)

	if not result:
		print "No result returned"
		return
	
	result_dom = fromstring(result.content)
  
  	print len(result_dom.xpath("body"))
	print len(result_dom.xpath("//div"))
  
  	results = result_dom.xpath("//ul[@id='searchresults']")
  	print len(results)


search(month)

