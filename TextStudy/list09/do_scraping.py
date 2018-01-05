import urllib.request
from bs4 import BeautifulSoup
req = urllib.request.urlopen('https://quality-start.in/company')
soup = BeautifulSoup(req,"html.parser")
print(soup.find('h1').text)
print(soup.find('h2').text)
print(soup.find('h3').text)
print(soup.find('h4').text)
#print(soup.find('h5').text)
#print(soup.find('h6').text)
