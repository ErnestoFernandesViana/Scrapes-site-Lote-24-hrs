from bs4 import BeautifulSoup
import requests
import re

def winner_scrap(html):
    '''scrap winners name'''
    data = requests.get(html)
    soup = BeautifulSoup(data.text, 'html.parser')


    data = soup.find_all("div","ExtSubInf2")
    regex = re.compile(r'(?:"L_UltimoLogin_\d+">)(.+)(?:</div>)', re.DOTALL)
    matches = re.findall(regex,str(data))
    matches_list = matches[0].split(',')
    regex_names = re.compile(r'(?:\t\t\t)(.+)\t\t')
    full_list = []
    str.split
    for match in matches_list:
        m = re.search(regex_names, match)
        try:
            full_list.append(m.group(1))
        except:
            full_list.append('email')
    return full_list

def price_scrap(html):
    '''scrap values they got'''
    data = requests.get(html)
    soup = BeautifulSoup(data.text, 'html.parser')
    data = soup.find_all("div","ExtSubInf3")
    regex = re.compile(r'[R$]{2}\s.+\t')
    matches = re.findall(regex,str(data))
    return [x.rstrip() for x in matches]
