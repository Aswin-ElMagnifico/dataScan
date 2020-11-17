from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'https://www.accessdata.fda.gov/CMS_IA/'
client = urlopen('https://www.accessdata.fda.gov/CMS_IA/iapublishdate.html')
page = client.read()
client.close()

soup = BeautifulSoup(page,'html.parser')

table_contents = soup.find('table')

html_references = table_contents.findAll('a',{})
URLs = []

for links in html_references:
    print(links.text)
    URLs.append(url+links['href'])

print(URLs)