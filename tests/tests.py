import pytest
from trainee_qa_auto.parse_table import WebsiteData, parsing_table


@pytest.mark.parametrize(
    'expected',
    [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 10**9, 1.5 * 10**9],
)
def test_most_popular_programming_language(expected):
    ...
