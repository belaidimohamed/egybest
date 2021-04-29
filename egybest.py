from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"/home/mohamed/Desktop/egybest/chromedriver") #incase you are chrome

def initSeries(url): #return a dict containing general informations about the serie
    driver.get(url)
    data = {}
    content = driver.page_source
    soup = BeautifulSoup(content)
    data['name'] = soup.find('td', attrs={'class':'movie_title'}).find('h1').getText()
    data['rate'] = soup.find('span', attrs={'itemprop':'ratingValue'}).getText()
    index = soup.findAll('div', attrs={'class':'pda'}).index(soup.find('div', attrs={'class':'pda'},text="القصة")) + 1 #because the description is just under the القصة tag

    data['description' ] = soup.findAll('div', attrs={'class':'pda'})[index].getText()
    data['seasons_count'] = len(soup.find('div', attrs={'class':'contents movies_small'}))
    links = [a['href'] for a in reversed(soup.find('div', attrs={'class':'contents movies_small'}).findAll('a',href=True))]
    data['seasons'] = links
    print(data , '\n')
    return data


def ScanSeason(url):
    driver.get(url)
    data = {}
    content = driver.page_source
    soup = BeautifulSoup(content)
    data['episods_count'] = len(soup.find('div', attrs={'class':'movies_small'}))
    data['episods'] = [a['href'] for a in reversed(soup.find('div', attrs={'class':'movies_small'}).findAll('a',href=True))]
    print(data)
def ScanEpisode(url):
    driver.get(url)
    data = {}
    content = driver.page_source
    soup = BeautifulSoup(content)
    data['episods_count'] = len(soup.find('div', attrs={'class':'dls_table btns full mgb'}))

general = initSeries("https://seen.egybest.ltd/series/the-resident-2018/?ref=tv-p1")
for i in general['seasons'] :
    ScanSeason(i)