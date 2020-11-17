from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/Driver/chromedriver.exe')
driver.get('https://datadashboard.fda.gov/ora/firmprofile.htm?FEIu=3002808636')
time.sleep(15)
page = driver.page_source
soup = BeautifulSoup(page,'html.parser')
insp_container = soup.findAll('div',{'id':'QVProfilesInspectionDetails'})

a = insp_container[0].findAll('tr',{'class':'qv-st-data-row ng-scope qv-grid-object-data-first-row qv-grid-object-data-last-row'})
tc = []
inspection_details = []
inspection_citation_details = []
recall_details = []

for contents in a:
    tc = contents.findAll('td',{})

    for element in tc:
        try:
            text = element.div.div.span.text
            inspection_details.append(text)
        except:
            pass

insp_container = soup.findAll('div',{'id':'QVProfilesCitationsDetails'})
a = insp_container[0].findAll('tr',{'class':'qv-st-data-row ng-scope qv-grid-object-data-first-row qv-grid-object-data-last-row'})


for contents in a:
    tc = contents.findAll('td',{})
    for element in tc:
        try:
            text = element.div.div.span.text
            inspection_citation_details.append(text)
        except:
            pass


insp_container = soup.findAll('div',{'id':'QVRefusalsByProductsDetails'})
a = insp_container[0].findAll('tr',{})


for contents in a:
    tc = contents.findAll('td',{})
    for element in tc:
        try:
            text = element.div.div.span.text
            recall_details.append(text)
        except:
            pass


print("\n\n\n")
print(inspection_details)
print(inspection_citation_details)
print(recall_details)



driver.close()