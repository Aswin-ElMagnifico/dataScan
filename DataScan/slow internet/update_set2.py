import time
import pickle
from bs4 import BeautifulSoup
from selenium import webdriver
import FDAClass

fei_list = open("fei_dataset.txt",'r')
dataset = open("dataset_2.dat",'ab')
inspection_details = []
inspectionc_details = []
compilance_details = []
recall_details = []
refusal_details = []
warning_details = []
container = []

for fei_id in fei_list:
    try:
        temp = fei_id.split()
        fei_identifier = temp[0]
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(executable_path=r'C:/Driver/chromedriver.exe', chrome_options=options)
        driver.get('https://datadashboard.fda.gov/ora/firmprofile.htm?FEIu=' + fei_identifier)
        time.sleep(15)
        page = driver.page_source
        soup = BeautifulSoup(page, 'lxml')
        driver.close()
        try:
            insp = soup.find('div', {'id': 'QVProfilesInspectionDetails'})
            table = insp.find('table', {'ng-style': 'tableStyles.content'})
            rows = table.findAll('tr', {})
            for row in rows:
                elements = row.findAll('td', {})
                for element in elements:
                    container.append(str(element.text).strip())
                inspection_details.append(container)
                container = []
        except:
            pass

        try:
            inspc = soup.find('div', {'id': 'QVProfilesCitationsDetails'})
            table = inspc.find('table', {'ng-style': 'tableStyles.content'})
            rows = table.findAll('tr', {})
            for row in rows:
                elements = row.findAll('td', {})
                for element in elements:
                    container.append(str(element.text).strip())
                inspectionc_details.append(container)
                container = []
        except:
            pass

        try:
            comp = soup.find('div', {'id': 'QVProfilesComplianceDetails'})
            table = comp.find('table', {'ng-style': 'tableStyles.content'})
            rows = table.findAll('tr', {})
            for row in rows:
                elements = row.findAll('td', {})
                for element in elements:
                    container.append(str(element.text).strip())
                compilance_details.append(container)
                container = []
        except:
            pass

        try:
            reca = soup.find('div', {'id': 'QVRecallsDetails'})
            table = reca.find('table', {'ng-style': 'tableStyles.content'})
            rows = table.findAll('tr', {})
            for row in rows:
                elements = row.findAll('td', {})
                for element in elements:
                    container.append(str(element.text).strip())
                recall_details.append(container)
                container = []
            print(recall_details)

        except:
            pass

        try:
            ref = soup.find('div', {'id': 'QVRefusalsByProductsDetails'})
            table = ref.find('table', {'ng-style': 'tableStyles.content'})
            rows = table.findAll('tr', {})
            for row in rows:
                elements = row.findAll('td', {})
                for element in elements:
                    container.append(str(element.text).strip())
                refusal_details.append(container)
                container = []

        except:
            pass

        try:
            warning_container = soup.findAll('div', {'class': 'graph_container nobg'})
            plain_text = warning_container[warning_container.__len__() - 1].find('div', {'class': 'col-xs-12 col-md-6'})
            lst = plain_text.text.split('\n')
            warning_details.append(plain_text.a['href'])
            warning_details.append(lst[0][lst[0].index('Subject:'):lst[0].index('Issue Date:')])
            warning_details.append(lst[0][lst[0].index('Issue Date:'):lst[0].index('Snippet:')])
        except:
            pass

        firm = FDAClass.FEIContainer(fei_identifier, inspection_details, inspectionc_details, compilance_details, recall_details, refusal_details,
                                     warning_details)
        pickle.dump(firm, dataset, pickle.HIGHEST_PROTOCOL)
    except:
        pass


fei_list.close()
dataset.close()
