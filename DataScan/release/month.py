from flask import Flask, render_template,request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = 'https://www.accessdata.fda.gov/CMS_IA/'
src_client = urlopen('https://www.accessdata.fda.gov/CMS_IA/iapublishdate.html')
rpage = src_client.read()
src_client.close()

soup1 = BeautifulSoup(rpage,'html.parser')
table_contents = soup1.find('table')
html_references = table_contents.findAll('a',{})

URLs = []
months = {'january':'01', 'feburary':'02', 'march':'03', 'april':'04', 'may':'05', 'june':'06', 'july':'07','august':'08', 'september':'09', 'october':'10', 'november':'11', 'december':'12'}
for links in html_references:
    URLs.append([links.text, url+links['href']])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/search')
def index1():
    firm_name = request.args.get('name')
    resultset = []
    print("Search querry:" + firm_name.lower() + " " + months[firm_name.lower()])
    for links in URLs:
        try:
            print("Downloading page: " + links[1])
            client = urlopen(links[1])
            page = client.read()
            client.close()
            print("Searching in page ", URLs.index(links) +1 ,"/",URLs.__len__()," "+links[1])
            page_container = BeautifulSoup(page, 'html.parser')
            container = page_container.findAll('div', {'class': 'div-info'})

            for firms in container:
                content = firms.find_all('div')
                date_container = content[1].text.split()
                date = date_container[3]
                print('matching with '+ date)
                try:
                    month = months[firm_name.lower()]
                    print("this: " + month +" with:"+date)
                    if (re.search('^'+month+'/*', date, re.IGNORECASE)):
                        print("Firm: ", content[0].text, "\n\t found in import alert: ", links[0], "\n", content[1].text)
                        resultset.append([content[0].text, links[0], content[1].text])
                        break
                except Exception:
                    pass

        except:
            pass

    if len(resultset) > 0:
        return render_template("ResultSet.html",firm=firm_name, resultset=resultset)
    else:
        return render_template("empty.html",firm_name=firm_name)

if __name__ == "__main__":
    app.run(debug=True)
