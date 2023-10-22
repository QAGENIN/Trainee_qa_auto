import re

import pytest
from trainee_qa_auto.parse_table import parsing_table


@pytest.mark.parametrize(
    'expected',
    [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 10**9, 1.5 * 10**9],
)
def test_most_popular_programming_language(expected):
    data_list = parsing_table()
    pattern = r'\[[^\]]+\]'
    for data in data_list:
        try:
            assert int(data.popularity) > expected
        except AssertionError:
            print(
                f'\n\n{data.company} (Frontend:{re.sub(pattern, "", data.front_end)} | Backend:{re.sub(pattern, "", data.back_end)}) has {data.popularity} unique visitors per month.(Expected more than {expected})\n\n'
            )
