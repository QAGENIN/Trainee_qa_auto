import re

import pytest
from trainee_qa_auto.parse_table import parsing_table

website_table = parsing_table()
test_value_list = [
    10**7,
    1.5 * 10**7,
    5 * 10**7,
    10**8,
    10**9,
    1.5 * 10**9,
]


@pytest.mark.parametrize('website', website_table)
def test_most_popular_programming_language(website):
    pattern = r'\[[^\]]+\]'
    mistakes = []
    for value in test_value_list:
        if int(website.popularity) < value:
            mistakes.append(
                f'{website.company}(Frontend:{re.sub(pattern, "", website.front_end)} | Backend:{re.sub(pattern, "", website.back_end)} has '
                f'{website.popularity} unique visitors per month. (expected more than {value})'
            )
        assert not mistakes, '\n'.join(mistakes)
