from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"/home/mohamed/Desktop/egybest/chromedriver") #incase you are chrome
driver.get('https://seen.egybest.ltd/episode/the-resident-2018-season-4-ep-1/?ref=tv-p1')
content = driver.page_source
data = {}
data['ep1'] = []
soup = BeautifulSoup(content)
qualite_table = soup.find('table', attrs={'class':'dls_table btns full mgb'}).tbody

x = qualite_table.findAll('tr')
ex = x[0].findAll('td')
data['ep1'].append([
                ex[1].getText(),
                ex[2].getText()
            ])
link = driver.find_element_by_l31xt(ex[3].find('a')['data-url'])
