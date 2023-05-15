import requests
from bs4 import BeautifulSoup
import csv
from modules.web_scraping import scrape_page
from modules.web_scraping import scraping_all_page
# the url of the home page of the target website
base_url = 'https://quotes.toscrape.com'

# defining the User-Agent header to use in the GET request below
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# retrieving the target web page
page = requests.get(base_url, headers=headers)

# parsing the target web page with Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')

# initializing the variable that will contain
# the list of all quote data
quotes = []

# scraping the home page
scrape_page(soup, quotes)

# getting the "Next →" HTML element
next_li_element = soup.find('li', class_='next')

scraping_all_page(soup, next_li_element, base_url, headers, quotes)

# reading  the "quotes.csv" file and creating it
# if not present
csv_file = open('./data/quotes.csv', 'w', encoding='utf-8', newline='')

# initializing the writer object to insert data
# in the CSV file
writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['Text', 'Author', 'Tags'])

# writing each row of the CSV
for quote in quotes:
    writer.writerow(quote.values())

# terminating the operation and releasing the resources
csv_file.close()