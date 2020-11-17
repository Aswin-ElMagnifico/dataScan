import openpyxl
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


workbook = openpyxl.load_workbook('AllDataSets.xlsx')
worksheet = workbook['Import Alerts']

firm_name = str(input('Please input a firm name: '))