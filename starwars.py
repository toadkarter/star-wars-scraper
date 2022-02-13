import requests, calendar
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date


class WikiToDfConverter():
    @classmethod
    def create_dataframe_from_url(cls):
        wiki_html = cls._pull_html_from_wookipedia()
        wiki_soup = cls._get_soup_object_from_html(wiki_html)
        raw_df = cls._create_dataframe_from_soup_object(wiki_soup)
        return cls._create_clean_dataframe(raw_df)

    def _pull_html_from_wookipedia():
        url = "https://starwars.fandom.com/wiki/Timeline_of_canon_media" 
        response = requests.get(url)
        return response.text

    def _get_soup_object_from_html(wiki_html):
        soup = BeautifulSoup(wiki_html, 'html.parser')
        return str(soup.find("table", class_='sortable'))

    def _create_dataframe_from_soup_object(wiki_soup):
        df = pd.read_html(str(wiki_soup))
        return pd.DataFrame(df[0])

    def _create_clean_dataframe(raw_df):
        raw_df.rename(columns={'Unnamed: 1':'Format'}, inplace=True )
        raw_df["Released"] = pd.to_datetime(raw_df["Released"], errors="coerce")
        clean_df = raw_df.sort_values(by="Released")
        return clean_df



df = WikiToDfConverter.create_dataframe_from_url()

current_date = date.today()
current_day = date.today().day
current_year = date.today().year
current_month = date.today().month

max_month_day = calendar.monthrange(current_year, current_month)[1]

month_limit=str(current_year)+str(current_month).zfill(2)+str(max_month_day).zfill(2)

current_date = pd.to_datetime(current_date)
month_limit = pd.to_datetime(month_limit)


month_range = (df["Released"] > current_date) & (df["Released"] <= month_limit)


releases_today = df[df["Released"]==str(date.today())]
releases_month = df[month_range]

def print_releases(releases):
    """TBC how this is going to be formatted"""
    print(releases["Title"])

print("Releases coming out today:")

if releases_today.empty:
    print("No releases today")
else:
    print_releases(releases_today)
print()
print("Releases coming out in the rest of the month:")

if releases_month.empty:
    print("No releases in the rest of the month")
else:
    print_releases(releases_month)
