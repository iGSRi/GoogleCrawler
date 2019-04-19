from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd

import numpy as np
count = 0
query = input("\n\n\n******************* - Welcome to Google Crawler. - *******************\n\n             Enter text to search >>")
print("             Please wait... Extracting top 10 results(URLs)...")
query = query.strip().split()
query = "+".join(query)

html = "https://www.google.co.in/search?site=&source=hp&q=" + query + "&gws_rd=ssl"
req = urllib.request.Request(html, headers = {'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(urlopen(req).read(),"html.parser")

#Regex
reg = re.compile(".*&sa=")

Data=[]
#Parsing Headings
for item in soup.find_all('h3'):
    Data.append([item.text])

links=[]
#Parsing web urls
for item in soup.find_all('h3', attrs={'class' : 'r'}):
    #line = (reg.match(item.a['href'][7:]).group())
    #links.append(line[:-4])
    links.append(item.a['href'][7:])

#Adding data to dictionary
Dict = {'Data': Data, 'URL': links}

#print(Dict)

#Adding data to DataFrame
my_def = pd.DataFrame(Dict)

#print(my_def)
my_def.to_csv('Extracted Result.csv', index = False, header = True)

print("             .\n             .\n             .\n             .\n\n             Output has been saved to -> C:\IRIS\Python\Google Search\Extracted  sult.csv \n\n\n******************* - Thanks! - *******************")
#print(links[1])