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
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find('table', {'class': 'wikitable sortable'})

    data_list = []

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > 0:
            company_name = columns[0].get_text().strip()
            values = [column.get_text().strip() for column in columns]

            popularity = (
                values[1].replace(',', '') if values[1] != 'None' else 'None'
            )
            front_end = values[2]
            back_end = values[3]
            database = values[4]
            notes = values[5]

            data = WebsiteData(
                company_name, popularity, front_end, back_end, database, notes
            )
            data_list.append(data)
