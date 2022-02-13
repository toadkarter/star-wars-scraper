from wikitodf import WikiToDfConverter
from releasesbydate import ReleasesInDateRange


df = WikiToDfConverter.create_dataframe_from_url()

dates = ReleasesInDateRange()
releases_today = dates.get_releases_today(df)
releases_this_month = dates.get_releases_this_month(df)


def print_releases(releases):
    """TBC how this is going to be formatted"""
    print(releases["Title"].head())


print("Releases coming out today:")

if releases_today.empty:
    print("No releases today")
else:
    print_releases(releases_today)
print()
print("Releases coming out in the rest of the month:")

if releases_this_month.empty:
    print("No releases in the rest of the month")
else:
    print_releases(releases_this_month)
