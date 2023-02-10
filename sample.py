import trafilatura
downloaded = trafilatura.fetch_url('https://www.afghanistannews.net/news/273495805/banks-risks-from-adani-group-exposure-limited-but-may-increase-moody')
data=trafilatura.extract(downloaded)
print(data)