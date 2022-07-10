from bs4 import BeautifulSoup
import re
import io
import pdfplumber
import requests

def change_chars(string):
    if 'ქ' in string: string = string.replace('ქ', 'q')
    if 'წ' in string: string = string.replace('წ', 'w')
    if 'ე' in string: string = string.replace('ე', 'e')
    if 'რ' in string: string = string.replace('რ', 'r')
    if 'ტ' in string: string = string.replace('ტ', 't')
    if 'ყ' in string: string = string.replace('ყ', 'y')
    if 'უ' in string: string = string.replace('უ', 'u')
    if 'ი' in string: string = string.replace('ი', 'i')
    if 'ო' in string: string = string.replace('ო', 'o')
    if 'პ' in string: string = string.replace('პ', 'p')
    if 'ა' in string: string = string.replace('ა', 'a')
    if 'ს' in string: string = string.replace('ს', 's')
    if 'დ' in string: string = string.replace('დ', 'd')
    if 'ფ' in string: string = string.replace('ფ', 'f')
    if 'გ' in string: string = string.replace('გ', 'g')
    if 'ჰ' in string: string = string.replace('ჰ', 'h')
    if 'ჯ' in string: string = string.replace('ჯ', 'j')
    if 'კ' in string: string = string.replace('კ', 'k')
    if 'ლ' in string: string = string.replace('ლ', 'l')
    if 'ზ' in string: string = string.replace('ზ', 'z')
    if 'ხ' in string: string = string.replace('ხ', 'x')
    if 'ც' in string: string = string.replace('ც', 'c')
    if 'ვ' in string: string = string.replace('ვ', 'v')
    if 'ბ' in string: string = string.replace('ბ', 'b')
    if 'ნ' in string: string = string.replace('ნ', 'n')
    if 'მ' in string: string = string.replace('მ', 'm')
    if 'ჭ' in string: string = string.replace('ჭ', 'W')
    if 'ღ' in string: string = string.replace('ღ', 'R')
    if 'თ' in string: string = string.replace('თ', 'T')
    if 'შ' in string: string = string.replace('შ', 'S')
    if 'ჟ' in string: string = string.replace('ჟ', 'J')
    if 'ძ' in string: string = string.replace('ძ', 'Z')
    if 'ჩ' in string: string = string.replace('ჩ', 'C')
    return string

def reverse_change(string):
    if 'q' in string: string = string.replace('q', 'ქ')
    if 'w' in string: string = string.replace('w', 'წ')
    if 'e' in string: string = string.replace('e', 'ე')
    if 'r' in string: string = string.replace('r', 'რ')
    if 't' in string: string = string.replace('t', 'ტ')
    if 'y' in string: string = string.replace('y', 'ყ')
    if 'u' in string: string = string.replace('u', 'უ')
    if 'i' in string: string = string.replace('i', 'ი')
    if 'o' in string: string = string.replace('o', 'ო')
    if 'p' in string: string = string.replace('p', 'პ')
    if 'a' in string: string = string.replace('a', 'ა')
    if 's' in string: string = string.replace('s', 'ს')
    if 'd' in string: string = string.replace('d', 'დ')
    if 'f' in string: string = string.replace('f', 'ფ')
    if 'g' in string: string = string.replace('g', 'გ')
    if 'h' in string: string = string.replace('h', 'ჰ')
    if 'j' in string: string = string.replace('j', 'ჯ')
    if 'k' in string: string = string.replace('k', 'კ')
    if 'l' in string: string = string.replace('l', 'ლ')
    if 'z' in string: string = string.replace('z', 'ზ')
    if 'x' in string: string = string.replace('x', 'ხ')
    if 'c' in string: string = string.replace('c', 'ც')
    if 'v' in string: string = string.replace('v', 'ვ')
    if 'b' in string: string = string.replace('b', 'ბ')
    if 'n' in string: string = string.replace('n', 'ნ')
    if 'm' in string: string = string.replace('m', 'მ')
    if 'W' in string: string = string.replace('W', 'ჭ')
    if 'R' in string: string = string.replace('R', 'ღ')
    if 'T' in string: string = string.replace('T', 'თ')
    if 'S' in string: string = string.replace('S', 'შ')
    if 'J' in string: string = string.replace('J', 'ჟ')
    if 'Z' in string: string = string.replace('Z', 'ძ')
    if 'C' in string: string = string.replace('C', 'ჩ')
    return string

url = 'https://info.police.ge/page?id=115'
src = requests.get(url)

output = io.BytesIO()
soup = BeautifulSoup(src.content, 'lxml')
urls = []

for article in soup.find_all('div'):
    try:
        link = article.find('a', href=True)['href']
        if '/page?' in link:
            urls.append(f'https://info.police.ge{link}')
    except Exception as e:
        break

temp_urls = []

for x in range(len(urls)):
    url = urls[x]
    src = requests.get(url)
    soup = BeautifulSoup(src.content, 'lxml')
    for article in soup.find_all('p'):
        try:
            link = article.find('a', href=True)['href']
            if '../' in link:
                temp_urls.append(f'https://info.police.ge/{link[3:]}')
                break
            else: 
                temp_urls.append(link)
                break
        except Exception as e:
            break

sub_url = list(dict.fromkeys(temp_urls))

r = re.compile("([a-zA-Z]+)([0-9]+)")
text = str(input('Enter text for search: '))
string_m = ''
for x in range(len(sub_url)):
    pdf_content = io.BytesIO(requests.get(sub_url[x]).content)
    read = pdfplumber.open(pdf_content)
    for i in range(len(read.pages)):
        lines = read.pages[i].extract_text().split("\n")
        for j in lines:
            if 'წელი' in j:
                year = j.split(" ")
            if reverse_change(text) in j:
                m = re.split('(\d+)',change_chars(j))
                for y in m:
                    string_m += y
                for o in m:
                    for b in o:
                        if b.isalpha():
                            print(f'დანაშაულის სახეობა:{reverse_change(o)[:-4]}')
                            break
                k = string_m.split('m.')[1]
                print('-' * 40)
                print(f'წელი: {year[2]}')
                print(f'სულ რეგისტრირებულია: {k.split(" ")[5]}')
                print(f'გახსნილია: {k.split(" ")[6]}')
                print(f'გახსნის %: {k.split(" ")[7]}')
                print('-' * 40)
                print(f'წელი: {year[0]}')
                print(f'სულ რეგისტრირებულია: {k.split(" ")[2]}')
                print(f'გახსნილია: {k.split(" ")[3]}')
                print(f'გახსნის %: {k.split(" ")[4]}')
                print('-' * 40)
                print('დანაშაულის მატება/კლება')
                print('-' * 40)
                print(f'+/- რაოდენობრივი %: {k.split(" ")[8]}')
                print(f'+/- პროცენტული %: {k.split(" ")[9]}')
                break