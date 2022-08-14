import pandas as pd
import requests
import feedparser
from bs4 import BeautifulSoup
import database as db
import desc_getter as dg
import os
from googletrans import Translator
import time
translator = Translator()

# Hello World


# getting database variables
languages = db.languages
regid = db.regid
lang_reg = db.lang_reg
abbr = db.abbr




# _________________________________Set url of data____________________________________________
def set_url(lang,regid):
    return f'https://pib.gov.in/RssMain.aspx?ModId=6&Lang={lang}&Regid={regid}'
    
# ____________________________Get data from url__________________________________

def get_data(url):    
    result = requests.get(url)
    data = feedparser.parse(result.text)
    return data['entries']

# _______________________Get data Description____________________________________            


# __________________________________Create dataframe____________________
def create_df(url,lang):
    flag = 0
    data = get_data(url)
    database = db.db
    entries = []
    Date = ''
    desc = ''
    for i in range(len(data)):

        if database.child('News').child(lang).child(data[i]['link'][-7:]).get().val():
            print("Already There...")
            break

        
        res = requests.get(data[i]['link'])
        d = feedparser.parse(res.text)

        bs4_html = BeautifulSoup(d['feed']['summary'], "html.parser")
        date = bs4_html.find('div',{'class':'ReleaseDateSubHeaddateTime'}).text
        date = date.split()
        Date = f'{date[2]} {date[3]} {date[4]}'
        time = date[5]
        pib = f'{date[7]} {date[8]}'

        try:
            desc = dg.get_desc(data[i]['link'])
        except Exception as e:
            print(e)
            

       
        database.child('News').child(lang).child(data[i]['link'][-7:]).set({'Date':Date,'Time':time,'Title':data[i]['title'],'Posted by':pib,'Link':data[i]['link'],"Description":desc})
        entries.append([Date,time,data[i]['title'],pib,data[i]['link']])

    df = pd.DataFrame(entries,columns=['Date','Time','Title','Posted by','Link'])
    return  df,Date


#__________________________________Craete dataframe file________________________________
#  

def create_file(df,date,lang,lang_reg):
    
    storage = db.storage
# as admin
   
    df.to_csv(f'{date}_{lang_reg}_{lang}.csv')
    storage.child(f'news_data/{date}_{lang_reg}_{lang}.csv').put(f'{date}_{lang_reg}_{lang}.csv')
    os.remove(f'{date}_{lang_reg}_{lang}.csv')



#___________________________________Fetch all data_________________________________________
def fetch_data():
    for i in languages:
        language = languages[i]
        reg_id = regid[lang_reg[i]]
        url = set_url(language,reg_id)
        df,date = create_df(url,i)
        print(i)
        create_file(df,date,i,lang_reg[i])



# lang = languages["Marathi"]
# reg_id = regid[lang_reg["Marathi"]]
# url = set_url(lang,reg_id)
# df,date = create_df(url,lang,reg_id)
# create_file(df,date,"Marathi",lang_reg["Marathi"])



if __name__ == '__main__':
    while(True):
        print('Fetching.....')
        fetch_data()
        print("Fetched")
        time.sleep(300)