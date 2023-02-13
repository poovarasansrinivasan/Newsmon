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
mycol = mydb["singaporenews"]

driver = webdriver.Chrome (executable_path="C:\chromedriver.exe")
driver.get("https://www.singaporenews.net/")
sleep(1)

def sample():
    data=driver.find_element(By.XPATH,'//*[@id="navigation-menu"]/div/ul/li[3]/a')
    data.click()
    sleep(2)
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        fin=soup.findAll('div',class_='media-object')
        print(len(fin))
        for post in fin:
            url = 'https://www.singaporenews.net'+ post.find('a')['href']  
            print(url)
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
                    mycol.insert_one(finaldict)
                except Exception as e:
                    pass
            else:
                continue
    except Exception as e:
        print(e)        
sample()