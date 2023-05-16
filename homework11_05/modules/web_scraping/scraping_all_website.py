from modules.web_scraping import scrape_page
import requests
from bs4 import BeautifulSoup

def scraping_all_page(soup, next_li_element, base_url, headers, quotes):

# if there is a next page to scrape
     while next_li_element is not None:
         next_page_relative_url = next_li_element.find('a', href=True)['href']

    # getting the new page
         page = requests.get(base_url + next_page_relative_url, headers=headers)

    # parsing the new page
         soup = BeautifulSoup(page.text, 'html.parser')

    # scraping the new page
         scrape_page(soup, quotes)

    # looking for the "Next →" HTML element in the new page
         next_li_element = soup.find('li', class_='next')