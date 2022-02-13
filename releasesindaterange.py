import calendar
import pandas as pd
from datetime import date

class ReleasesInDateRange():
    def __init__(self):
        self._date = date.today()
        self._year = self._date.year
        self._month = self._date.month
        self._day = self._date.day

    def get_releases_today(self, df):
        """Selects releases from the dataframe that have come out today"""
        today = self._get_today_as_datetime()
        day_range = df["Released"]==today
        return df[day_range]

    def get_releases_this_month(self, df):
        """Selects releases from the dataframe that will come out by the end of the month"""
        today = self._get_today_as_datetime()
        end_of_month = self._get_end_of_month_as_datetime()
        month_range = (df["Released"] > today) & (df["Released"] <= end_of_month)
        return df[month_range]

    def _get_today_as_datetime(self):
        """Returns today's date as a datetime object"""
        today = str(self._date)
        return pd.to_datetime(today)

    def _get_last_day_of_month_as_string(self):
        """Returns the last day of the current month as a string"""
        month_range = calendar.monthrange(self._year, self._month)
        return str(month_range[1])

    def _get_end_of_month_as_datetime(self):
        """"""
        last_day_of_month = self._get_last_day_of_month_as_string()
        end_of_month_as_string = str(self._year)+str(self._month).zfill(2)+last_day_of_month.zfill(2)
        return pd.to_datetime(end_of_month_as_string)