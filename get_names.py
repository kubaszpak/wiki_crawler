import requests
from bs4 import BeautifulSoup

link = input("Pass a link to a wikipedia page: ")

url = requests.get(link).text
soup = BeautifulSoup(url, "html.parser")
names = []
# print(soup.find_all("li"))

'''The next part is really specific to this web page
as I needed all car companies in a list'''

'''I have used this link https://pl.wikipedia.org/wiki/Kategoria:Marki_samochod%C3%B3w'''

soup = soup.find("div",class_="mw-category")
for x in soup.find_all("li"):
    try:
        name = x.text
        # if " (marka samochodów)" in name:
        #     name = name.replace(" (marka samochodów)","")
        # elif " (motoryzacja)" in name:
        #     name = name.replace(" (motoryzacja)","")
        # elif " (przedsiębiorstwo)" in name:
        #     name = name.replace(" (przedsiębiorstwo)","")
        names.append(name)
    except Exception:
        pass
    
print(names)
with open("test.txt",'w',encoding = 'utf-8') as f:
    for name in names:
        f.write(name + "\n")