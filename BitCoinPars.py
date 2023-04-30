a = 0
import time
import os
import pandas
import csv
def pars():
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent
    import requests
        
    url = "https://www.rbc.ru/crypto/currency/btcusd"
    head = {"User-Agent": UserAgent().random}
    #Insert the link and put a random user-agent

    requests = requests.get(url,head)
    soup = BeautifulSoup(requests.text, "html.parser")
    teme = soup.find_all('div', class_='chart__info')
    #Cooking Soup

    for temes  in teme:
        temes = temes.find("div", {'class' : 'chart__subtitle js-chart-value'})
        if temes is not None:
            url_title = (temes.text)
            url_title = url_title.split()
            url_title.pop(2)
            url_title.pop(2)
            url_title = "".join(url_title)
    #Article cursed

    for temes1  in teme:
        temes1 = temes1.find("span", {'class' : 'js-chart-date'})
        if temes1 is not None:
            url_date = (temes1.text)
    
    if not os.path.exists('bitcoin.csv'):
        with open('bitcoin.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["date","course"]
            writer.writerow(field)
    else:
        with open('bitcoin.csv', 'a', newline='') as file:
            write = csv.writer(file)
            field = [url_date, url_title]
            write.writerow(field)

while a != 1:
    pars()
    time.sleep(15)
    os.system('CLS') 