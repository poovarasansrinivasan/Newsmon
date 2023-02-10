from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pymongo
from newspaper import Article
import trafilatura
import pymongo
import hashlib
import uuid
from datetime import datetime


driver = webdriver.Chrome (executable_path="C:\chromedriver.exe")
driver.get("https://vietnam.vnanet.vn/english/making-news-p-43-1.html")
# driver.get("https://vietnam.vnanet.vn/english/")
sleep(2)
# driver.find_element(By.XPATH,'//*[@id="bavn-hd"]/section[2]/div/nav/div[1]/ul/li[3]/a').click()
# sleep(2)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newsmon"]
mycol = mydb["afghanistansun"]

def sample():
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        fin=soup.findAll('div',class_='uk-grid-margin uk-first-column')
        print(len(fin))
        for post in fin:
            url =post.find('a')['href']  
            # arr.append(url)
            print(url)
    except Exception as e:
        print(e)    
sample()        


