import requests
import pandas as pd
from bs4 import BeautifulSoup


class WikiToDfConverter:
    @classmethod
    def create_dataframe_from_url(cls):
        """Accesses Wookipedia and returns a clean Pandas dataframe of all future media"""
        wiki_html = cls._pull_html_from_wookipedia()
        wiki_soup = cls._get_soup_object_from_html(wiki_html)
        raw_df = cls._create_dataframe_from_soup_object(wiki_soup)
        return cls._create_clean_dataframe(raw_df)

    @staticmethod
    def _pull_html_from_wookipedia():
        """Accesses the Wookipedia future media page and returns the html of that page"""
        url = "https://starwars.fandom.com/wiki/Timeline_of_canon_media" 
        response = requests.get(url)
        return response.text

    @staticmethod
    def _get_soup_object_from_html(wiki_html):
        """Creates Beautiful Soup object from HTML text"""
        soup = BeautifulSoup(wiki_html, 'html.parser')
        return str(soup.find("table", class_='sortable'))

    @staticmethod
    def _create_dataframe_from_soup_object(wiki_soup):
        """Creates dataframe from a Beautiful Soup object"""
        df = pd.read_html(str(wiki_soup))
        return pd.DataFrame(df[0])

    @staticmethod
    def _create_clean_dataframe(raw_df):
        """Cleans the dataframe so that the data within it can be easily accessed"""
        raw_df.rename(columns={'Unnamed: 1': 'Format'}, inplace=True)
        raw_df["Released"] = pd.to_datetime(raw_df["Released"], errors="coerce")
        clean_df = raw_df.sort_values(by="Released")
        print(clean_df.head())
        return clean_df
