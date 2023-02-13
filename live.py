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
driver.get("https://www.livelaw.in/news-updates")
sleep(2)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newsmon"]
mycol = mydb["afghanislamicpress"]

def sample(): 
    for i in range(1, 51):
        print(i)
        driver.get (f"https://www.livelaw.in/news-updates/{i}")
        # Get scroll height
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while (match==False):
            lastCount = lenOfPage
            sleep(1)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
        try:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            fin=soup.findAll('div',class_='row row_right_padding flex')
            print(len(fin))
            for post in fin:
                url = post.find('a')['href']  
                print(url)      
        except Exception as e:
            print(e)        
sample()
  



     
  