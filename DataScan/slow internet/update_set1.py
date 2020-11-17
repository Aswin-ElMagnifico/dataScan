from bs4 import BeautifulSoup
from urllib.request import urlopen
import FDAClass
import pickle


_url = 'https://www.accessdata.fda.gov/CMS_IA/'
_src_client = urlopen('https://www.accessdata.fda.gov/CMS_IA/iapublishdate.html')
_rpage = _src_client.read()
_src_client.close()

_soup1 = BeautifulSoup(_rpage,'lxml')
_table_contents = _soup1.find('table')
_html_references = _table_contents.findAll('a',{})

URLs = []
for links in _html_references:
    URLs.append([links.text, _url+links['href']])

dataset = open("dataset_1.dat", "ab")

for  links in URLs:
    if(URLs.index(links) > 4):
        break
    print("Downloading page " + (URLs.index(links) + 1) + "/"+URLs.__len__())
    try:
        client = urlopen(links[1])
        page = client.read()
        client.close()

        page_container = BeautifulSoup(page, 'lxml')
        container = page_container.findAll('div', {'class': 'div-info'})

        for firms in container:
            content = firms.find_all('div')

            firm_object = FDAClass.Firms_import(content[0].text, links[0], links[1], content[1].text)
            pickle.dump(firm_object, dataset, pickle.HIGHEST_PROTOCOL)


    except:
        pass


dataset.close()