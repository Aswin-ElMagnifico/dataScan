from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path=r'C:/Driver/chromedriver.exe', chrome_options=options)
time.sleep(10)


