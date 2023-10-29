import re

import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class WebsiteData:
    company: str
    popularity: int
    front_end: str
    back_end: str
    database: str
    notes: str


def parsing_table():
    url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')

    table = soup.find('table', {'class': 'wikitable sortable'})

    website_data_list = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > 0:
            company_name = columns[0].get_text().strip()
            values = [column.get_text().strip() for column in columns]

            popularity = int(re.sub('[^0-9]', '', values[1].split('[')[0]))
            front_end = values[2]
            back_end = values[3]
            database = values[4]
            notes = values[5]

            data = WebsiteData(
                company_name, popularity, front_end, back_end, database, notes
            )
            website_data_list.append(data)
    return website_data_list
