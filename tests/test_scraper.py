from web_scraper.scraper import get_citations_needed_report
from web_scraper.scraper import get_citations_needed_count


def test_get_citations_needed_report():
    actual = get_citations_needed_report('https://en.wikipedia.org/wiki/Medicine_in_the_medieval_Islamic_world')
    expected = open ('./citation.txt','r').read()
    assert expected == actual

def test_get_citations_needed_count():
    expected = 12
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/Arabs')
    assert expected ==  actual