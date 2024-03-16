from bs4 import BeautifulSoup
import requests

url = 'https://www.geeksforgeeks.org/'
req  = requests.get(url) 

soup = BeautifulSoup(req.content, "html.parser")   

# print(soup.prettify())
# print(soup.get_text())

res = soup.title
print(res)
print(res.prettify()) # structured content , easily inspect and simplar to identify pattern
print(res.get_text())