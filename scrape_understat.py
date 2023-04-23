# import the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# define URL
url  = "https://understat.com"

# send an HTTP request to the URL and receive a response
response = requests.get(url)

# parse the response context and retrieve HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract necessary data from the webpage as per our requirement
#get all the script tags in html contents
scripts = soup.find_all('script')

# search for the data tag
script = scripts[1]
data = script.string.strip()

# process the data using regex
import re
data = re.sub(r'^s*vars+datas*=s*', '', data, flags=re.MULTILINE)
data = re.sub(r';s*$', '', data, flags=re.MULTILINE)

# convert the processed data to a pandas dataframe
data = pd.read_json(data)

# write the dataframe to a CSV file
data.to_csv('understat_data.csv', sep=',', index=False)
