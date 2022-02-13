import pandas as pd
import requests
from bs4 import BeautifulSoup
import codecs

"""
url = "https://starwars.fandom.com/wiki/Timeline_of_canon_media"
table_class = "wikitable sortable jquery-tablesorter"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
"""

# This wil obviously be changed to the above, this is just to avoid all the repetitive scraping
url = codecs.open("test.htm", "r", "utf-8")

soup = BeautifulSoup(url, 'html.parser')

media_table = soup.find("table", class_='sortable')

df = pd.read_html(str(media_table))
df = pd.DataFrame(df[0])

print(df)





