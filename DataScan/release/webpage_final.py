from flask import Flask, render_template,request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import time
from selenium import webdriver






_url = 'https://www.accessdata.fda.gov/CMS_IA/'
_src_client = urlopen('https://www.accessdata.fda.gov/CMS_IA/iapublishdate.html')
_rpage = _src_client.read()
_src_client.close()

_soup1 = BeautifulSoup(_rpage,'html.parser')
_table_contents = _soup1.find('table')
_html_references = _table_contents.findAll('a',{})

URLs = []
for links in _html_references:
    URLs.append([links.text, _url+links['href']])



app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home_page.html')




@app.route('/importalerts')
def importalearts():
    return render_template('importalerts.html')

@app.route('/search-imports')
def searchimportsfirm():
    firm_name = request.args.get('name')
    resultset = []
    print("Search querry: " + firm_name)
    for links in URLs:
        if URLs.index(links) > 5:
            break

        try:
            print("Downloading page: " + links[1])
            client = urlopen(links[1])
            page = client.read()
            client.close()
            page_container = BeautifulSoup(page, 'html.parser')
            container = page_container.findAll('div', {'class': 'div-info'})
            print("Searching in page ", URLs.index(links) + 1, "/", URLs.__len__())

            for firms in container:
                content = firms.find_all('div')

                if (re.search(firm_name, content[0].text, re.IGNORECASE)):
                    print("Firm: ", content[0].text, "\t found in import alert: ", links[0]," ",  content[1].text,"\n")
                    resultset.append([content[0].text, links[0], content[1].text])
                    break

        except:
            pass

    if len(resultset) > 0:
        return render_template("iafresults.html", firm=firm_name, resultset=resultset)
    else:
        return render_template("nil.html", firm_name=firm_name)











@app.route('/importmonth')
def importmonth():

    return render_template('importmonth.html')


@app.route('/search-months')
def searchmonth():
    months = {'january': '01', 'feburary': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06', 'july': '07',
              'august': '08', 'september': '09', 'october': '10', 'november': '11', 'december': '12'}
    month_year = request.args.get('name').split()
    month = month_year[0].lower()
    year = month_year[1]
    resultset = []
    for links in URLs:
        if URLs.index(links) > 3:
            break

        try:
            print("Downloading page: " + links[1])
            client = urlopen(links[1])
            page = client.read()
            client.close()
            page_container = BeautifulSoup(page, 'html.parser')
            container = page_container.findAll('div', {'class': 'div-info'})
            print("Searching in page ", URLs.index(links) + 1, "/", URLs.__len__())

            for firms in container:
                content = firms.find_all('div')
                date_container = content[1].text.split()
                date = date_container[3]
                format_date = months[month] + '/[0-3][0-9]/' + year

                if (re.search(format_date, date, re.IGNORECASE)):
                    print("Firm: ", content[0].text, "\t found in import alert: ", links[0]," ",  content[1].text,"\n")
                    resultset.append([content[0].text, links[0], content[1].text])


        except:
            pass

    if len(resultset) > 0:
        return render_template("iamresults.html", month=month_year[0] + " "+ month_year[1], resultset=resultset)
    else:
        return render_template("nil.html", firm_name=month_year[0] + " "+ month_year[1])








@app.route('/firmsearch')
def firmsearch():
    return render_template('firmsearch.html')

@app.route('/search-firms')
def searchfirm():
    inspection_details = []
    refusal_details = []
    warning_details = []
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path=r'C:/Driver/chromedriver.exe', chrome_options=options)
    fei = request.args.get('name')
    driver.get('https://datadashboard.fda.gov/ora/firmprofile.htm?FEIu=' + fei)
    time.sleep(15)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    driver.close()
    try:
        print("insp")
        insp_container = soup.findAll('div', {'id': 'QVProfilesInspectionDetails'})
        table_headers = insp_container[0].findAll('tr',{'class':'qv-st-data-row ng-scope qv-grid-object-data-first-row qv-grid-object-data-last-row'})
        for headers in table_headers:
            data = headers.findAll('td',{})
            for elements in data:
                try:
                    inspection_details.append(elements.div.div.span.text)
                except:
                    pass
        print("refu")
        refusal_container = soup.find('div', {'id': 'QVRefusalsByProductsDetails'})

        table_headers = refusal_container.findAll('tr',{})
        print(table_headers.__len__())
        temp = []
        for headers in table_headers:
            data = headers.findAll('td',{})
            for elements in data:
                try:
                    print(elements.div.div.span.text)
                    temp.append(elements.div.div.span.text)
                except:
                    pass
            refusal_details.append(temp)
            temp = []

        warning_container = soup.findAll('div',{'class':'graph_container nobg'})
        plain_text = warning_container[warning_container.__len__() -1].find('div',{'class':'col-xs-12 col-md-6'})
        lst = plain_text.text.split('\n')
        warning_details.append(plain_text.a['href'])
        warning_details.append(lst[0][lst[0].index('Subject:'):lst[0].index('Issue Date:')])
        warning_details.append(lst[0][lst[0].index('Issue Date:'):lst[0].index('Snippet:')])


    except:
        pass


    return render_template('fresults.html',insp=inspection_details, refu=refusal_details[1:], warn=warning_details, fei = fei)



if __name__ == "__main__":
   app.run(debug=True)