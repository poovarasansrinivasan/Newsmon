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
driver.get("https://www.kualalumpurnews.net/")
sleep(2)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newsmon"]
mycol = mydb["afghanistannews"]

def sample():
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        fin=soup.findAll('div',class_='single_head')
        print(len(fin))
        for post in fin:
            url ='https://www.kualalumpurnews.net'+post.find('a')['href']
            print(url)
            # url = url.strip()
            # hashofurl = hashlib.md5(url.encode()).hexdigest()
            # result = mycol.find_one({"hashlink":hashofurl})
            # if result == None:
            #     finaldict = dict()
            #     try:
            #         article = Article(url)
            #         try :
            #             article.download()
            #             article.parse()
            #             title = article.title
            #             pdate = article.publish_date
            #         except Exception as e:
            #             pass
        
            #         try:
            #             download = trafilatura.fetch_url(url)
            #             text = trafilatura.bare_extraction(download, with_metadata=True, url=url)
            #         except Exception as e:
            #             pass
            #         finaldict['_id'] = str(uuid.uuid4())
            #         finaldict['created_date'] = datetime.now()
            #         finaldict['url'] = url
            #         finaldict['title'] = title
            #         finaldict['publish_date'] = pdate
            #         finaldict['text'] = text
            #         finaldict['hashlink'] = hashofurl
            #         print(finaldict)
            #         x=list(mycol.find({"url":url}))
            #         if len(x)< 1:
            #             mycol.insert_one(finaldict)
            #         else:
            #             break    
            #         print (finaldict)
            #         # mycol.insert_one(finaldict)
            #     except Exception as e:
            #         pass
            # else:
            #     continue     
    except Exception as e:
        print(e) 
sample()        


