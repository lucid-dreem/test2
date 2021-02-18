import urllib.request
from bs4 import BeautifulSoup
import ssl
import string

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.who.int/news-room/q-a-detail/q-a-coronaviruses"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

soup = str(soup)

quest = input("What is the question? ")
quest = quest.lower()

translation = quest.maketrans('','',string.punctuation)
quest = quest.translate(translation)


quest = quest.split(' ')
soup = soup.split(' ')

for x in quest:
    if x in soup:
        print ('TRUE')
    else:
        print ('Sorry')
    
print ("Hello World again")
