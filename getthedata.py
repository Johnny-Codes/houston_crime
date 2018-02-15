from bs4 import BeautifulSoup as bs
import requests
import re
import csv
import wget
from pathlib import Path

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

### finds the filename from the url ie jan15.xls
file_list = []
for filename in excel_list:
    a = filename[-9:]
    file_list.append(a)

### Creates dictionary ('jan16.xls': 'url/xls/jan16.xls')
### so if the downloads are interrupted, you can rerun without
### redownloading files already downloaded.
dictionary = dict(zip(file_list, url_list))

for key, value in dictionary.items():
    if Path(key).exists():
        print(f"{key} exists. Skipping")
        pass
    else:
        print(f"\nDownloading {key}")
        wget.download(value)

###### What I learned #######
### How to iterate over links and then iterate them to get the href
### Requesting each file and saving to computer with wget
### How to iterate over a dictionary. I was having trouble...
### ...downloading and kept having to restart so I created a dictionary
### with the filename to check if it exists and skip if I had downloaded
### already.
### Also, how to make a dictionary out of two lists and parsing a list (line 30)
