from bs4 import BeautifulSoup as bs
import requests
import re
import csv
import wget

url = "http://www.houstontx.gov/police/cs/crime-stats-archives.htm"
r = requests.get(url)
soup = bs(r.content, 'html.parser')


### extracts the href for the file
excel_list = []
for x in soup:
    excel_file_links = soup.find_all(href=re.compile(".xls"))
    for y in excel_file_links:
        z = y.attrs['href']
        excel_list.append(z)

### creates the final url for each month of data
url_list = []
for filename in excel_list:
    urll = "http://www.houstontx.gov/police/cs/" + filename
    url_list.append(urll)

for document in url_list:
    filename = wget.download(document)


###### What I learned #######
### How to iterate over links and then iterate them to get the href
### Requesting each file and saving to computer with wget
