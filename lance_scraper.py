#functions for scraper script
from bs4 import BeautifulSoup
import requests
import json
from winner_scrap import winner_scrap, price_scrap
import re


def html_scraper(html_list,x):
    for html_string in html_list:
        try:
            data = requests.get(html_string)
        except:
            continue
        soup = BeautifulSoup(data.text, 'html.parser')
        regex_hrs = re.compile(r'\d{2}:\d{2}:\d{2}')
        regex_day = re.compile(r'\d{2}[/]\d{2}[/]\d{4}')
        str_t = r'^title(\.)'
        str_t2 = r'\t\t\t\t(.+)\t\t\t'
        regex_title = re.compile(str_t2)

        horas = re.findall(regex_hrs, str(soup.findAll('span')))
        days = re.findall(regex_day, str(soup.findAll('span')))
        names = re.findall(regex_title, str(soup.find_all('h3')))
        try:
            names_3 = [re.search(r'\w+\s\w+\s[a-zA-Z0-9.]+', x).group() for x in names]
        except:
            continue

        winner_list = winner_scrap(html_string)
        price_list = price_scrap(html_string)

        try:
            with open('./horas/horas'+str(x)+'.txt','a') as file:
                file.write(str(horas)+'\n')
            with open('./price/price'+str(x)+'.txt','a') as file:
                file.write(str(price_list)+'\n')
            with open('./days/days'+str(x)+'.txt','a') as file:
                file.write(str(days)+'\n')
            with open('./names/names'+str(x)+'.txt','a') as file:
                file.write(str(names_3)+'\n')
            with open('./winner/winner'+str(x)+'.txt','a') as file:
                file.write(str(winner_list)+'\n')

        except:
            continue

def update_data():
    html = 'https://www.lance24h.com.br/Leiloes_Arrematados.php?Pagina='
    htmls = [html + str(x) for x in range(1,50)]
    htmls2 = [html + str(x) for x in range(50,100)]
    htmls3 = [html + str(x) for x in range(100,150)]
    htmls4 = [html + str(x) for x in range(150,200)]
    htmls5 = [html + str(x) for x in range(200,250)]
    htmls6 = [html + str(x) for x in range(250,300)]

    h = htmls,htmls2,htmls3,htmls4,htmls5,htmls6
    for i, x in enumerate(h):
        html_scraper(x, i+1)

if __name__ == '__main__':
    update_data()
