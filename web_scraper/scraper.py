import requests
from bs4 import BeautifulSoup

def get_citations_needed_report(url):
    res = requests.get(url)
    page = BeautifulSoup(res.content,'html.parser') # converts res from bytes to string
    citation = page.find_all('a',title ="Wikipedia:Citation needed")

    repetions = 1
    output = ''
    for item in citation:
            if len(item.parent.parent.parent.get_text().split('[citation needed]')) > 2:
                repetions +=1
                if repetions == len(item.parent.parent.parent.get_text().split('[citation needed]')):
                    output+=  '\n' + '**Citation Needed**' +'\n' + item.parent.parent.parent.get_text().split('[citation needed]')[0] +'\n'
                    output+=  '\n' + '**Citation Needed**' +'\n' + item.parent.parent.parent.get_text().split('[citation needed]')[1] +'\n'
                continue
            
            else:
                output+= '\n' + '**Citation Needed**' +' \n' + item.parent.parent.parent.get_text().split('[citation needed]')[0] +'\n'
    with open('citation.txt', 'w') as f:
        f.write(output)
    return output

def get_citations_needed_count(url):
    res = requests.get(url)
    page = BeautifulSoup(res.content,'html.parser') # converts red from bytes to string
    citation = page.find_all('a',title ="Wikipedia:Citation needed")
    return len(citation)


if __name__ == '__main__':
    expected = open ('./citation.txt','r')
    get_citations_needed_count('https://en.wikipedia.org/wiki/Arabs')
    get_citations_needed_report ('https://en.wikipedia.org/wiki/Arabs')
    print(expected.read())

