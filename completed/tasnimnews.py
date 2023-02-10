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

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newsmon"]
mycol = mydb["tasnimnews"]

driver = webdriver.Chrome (executable_path="C:\chromedriver.exe")
driver.get("https://www.tasnimnews.com/en/top-stories")
sleep(1)

def sample():
    for i in range(1, 51):
        print(i)
        driver.get (f"https://www.tasnimnews.com/en/top-stories?page={i}")
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
            fin=soup.findAll('article',class_='list-item')
            for post in fin:
                url = 'https://www.tasnimnews.com'+ post.find('a')['href']  
                url = url.strip()
                hashofurl = hashlib.md5(url.encode()).hexdigest()
                result = mycol.find_one({"hashlink":hashofurl})
                if result == None:
                    finaldict = dict()
                    try:
                        article = Article(url)
                        try :
                            article.download()
                            article.parse()
                            title = article.title
                            pdate = article.publish_date
                        except Exception as e:
                            pass
            
                        try:
                            download = trafilatura.fetch_url(url)
                            text = trafilatura.bare_extraction(download, with_metadata=True, url=url)
                        except Exception as e:
                            pass
                        finaldict['_id'] = str(uuid.uuid4())
                        finaldict['created_date'] = datetime.now()
                        finaldict['url'] = url
                        finaldict['title'] = title
                        finaldict['publish_date'] = pdate
                        finaldict['text'] = text
                        finaldict['hashlink'] = hashofurl
                        print(finaldict)
                        x=list(mycol.find({"url":url}))
                        if len(x)< 1:
                            mycol.insert_one(finaldict)
                        else:
                            break    
                        print (finaldict)
                        # mycol.insert_one(finaldict)
                    except Exception as e:
                        pass
                else:
                    continue       
        except Exception as e:
            print(e)        
sample()