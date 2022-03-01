
from bs4 import BeautifulSoup
import requests
import pprint
import re


data = requests.get('https://www.lance24h.com.br/Leiloes_Arrematados.php?Pagina=2')
soup = BeautifulSoup(data.text, 'html.parser')


data = soup.find_all("div","ExtSubInf2")
regex = re.compile(r'(?:"L_UltimoLogin_\d+">)(.+)(?:</div>)', re.DOTALL)
#regex2 = re.compile(r'(?:\t\t\t)(.+)(?:\t\t</div)', re.DOTALL)
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


data = requests.get('https://www.lance24h.com.br/Leiloes_Arrematados.php?Pagina=2')
soup = BeautifulSoup(data.text, 'html.parser')
data = soup.find_all("div","ExtSubInf3")
regex = re.compile(r'[R$]{2}\s.+\t')
matches = re.findall(regex,str(data))



if __name__ == '__main__':
    #print(names)
    #print(str(matches[0]))
    print(data[0])
    print(matches)
    print([x.rstrip() for x in matches])
