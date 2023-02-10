import trafilatura
downloaded = trafilatura.fetch_url('https://www.businesstimes.com.sg/companies-markets/ocbc-unit-files-police-report-against-gudang-garam-owner')
data=trafilatura.extract(downloaded)
print(data)

# import pymongo
# from newspaper import Article
# import trafilatura
# import uuid
# from datetime import datetime
# import hashlib
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["newsmon"]
# mycol = mydb["indonesianews"]
# # file = open("/home/sensai/projects/serp_alibongo/result/final_/new_data/new_urls_data.json")
# file=['https://www.businesstimes.com.sg/companies-markets/ocbc-unit-files-police-report-against-gudang-garam-owner']
# # with open('/home/blackpanther/poovarasan/Newsmon/kualal.txt') as f:
# #     contents = f.readlines()
# #     print(contents)
# for url in file:
#     url = url.strip()
#     # print(url)
#     hashofurl = hashlib.md5(url.encode()).hexdigest()
#     result = mycol.find_one({"hashlink":hashofurl})
#     if result == None:
#         finaldict = dict()
#         # print(url)
#         try:
#             article = Article(url)
#             try :
#                 article.download()
#                 article.parse()
#                 title = article.title
#                 pdate = article.publish_date
#             except Exception as e:
#                 pass
#             try:
#                 download = trafilatura.fetch_url(url)
#                 text = trafilatura.bare_extraction(download, with_metadata=True, url=url)
#             except Exception as e:
#                 # print(e)
#                 pass
#             # print(text)
#             finaldict['_id'] = str(uuid.uuid4())
#             finaldict['created_date'] = datetime.now()
#             finaldict['url'] = url
#             finaldict['title'] = title
#             finaldict['publish_date'] = pdate
#             finaldict['text'] = text
#             finaldict['hashlink'] = hashofurl
#             print(finaldict)
#             mycol.insert_one(finaldict)
#         except Exception as e:
#             pass
#     else:
#         continue
        