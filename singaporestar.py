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
driver.get("https://www.singaporestar.com/")
sleep(2)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newsmon"]
mycol = mydb["afghanistansun"]

def sample():
    data=driver.find_element(By.XPATH,'//*[@id="navigation-menu"]/div/ul/li[2]/a')
    data.click()
    sleep(2)
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        fin=soup.findAll('div',class_='row collapse')
        print(len(fin))
        for post in fin:
            url ='https://www.singaporestar.com'+ post.find('a')['href'] 
            print(url)
    except Exception as e:
        print(e) 
sample()        


