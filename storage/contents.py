import sys
from os.path import dirname,abspath
import requests
import pandas as pd
from bs4 import BeautifulSoup
# import os
sys.path.append(dirname(dirname(abspath(__file__))))
from module.aricle import Aricle
def scapweb(url):
    r = requests.get(url)
    r.encoding = 'utf-8' 
    soup = BeautifulSoup(r.text,'lxml')
    title = soup.find_all('h1',{'class':'jsx-3943502238 title'})[0].text
    image_ = soup.find_all('img')
    display = image_[7]['src']
    detail = soup.find_all('p')
    str_ =''
    for i in range(len(detail)-6):
        str_ +=detail[i].text.strip()
    str_=str_.replace('\xa0',' ')
    str_=str_.replace('สนับสนุนเนื้อหา','')
    return Aricle(title=title,image=display,contents=str_)

def get_all_contents():
    url_=['https://www.sanook.com/game/1174290/','https://www.sanook.com/game/1173794/','https://www.sanook.com/game/1173802/','https://www.sanook.com/game/1173842/','https://www.sanook.com/game/1173978/',]
    arr=[]
    for i in url_:
        arr.append(scapweb(i))
    return arr

def get_all_contents2():
    df = pd.read_csv(r'C:/Users/Raum/Desktop/Dev/nlp/storage/data.csv',usecols=['title','image','contents'])
    arr=[]
    for i in range(len(df)):
        arr.append(Aricle(title=df.iloc[i,0],image=df.iloc[i,1],contents=df.iloc[i,2]))
    return arr


if __name__ == "__main__":
    print("hello world!!")
    # print(get_all_contents2())
    # print(os.listdir("C:/Users/Raum/Desktop/Dev/nlp/storage"))


    