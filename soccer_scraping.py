import requests
from bs4 import BeautifulSoup

def extract_data(url):
    ''' Extract data from given url '''
    data = []
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        ''' Extract data using bs4 '''
        ''' Some code to extract data '''
    return data


if __name__ == '__main__':
    url = 'https://understat.com'
    data = extract_data(url)
    print(data)