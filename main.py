from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

ZILLOW_URL = 'https://www.zillow.com/north-virginia-beach-virginia-beach-va/sold/house_type/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22North%20Virginia%20Beach%2C%20Virginia%20Beach%2C%20VA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-76.12085270996091%2C%22east%22%3A-75.9715073120117%2C%22south%22%3A36.823989603669176%2C%22north%22%3A36.9385050158866%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A246020%2C%22regionType%22%3A8%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A700000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3149%7D%2C%22sqft%22%3A%7B%22min%22%3A2000%7D%2C%22doz%22%3A%7B%22value%22%3A%227%22%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D'
ZILLOW_URL = 'https://www.zillow.com/north-virginia-beach-virginia-beach-va/sold/house_type/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22North%20Virginia%20Beach%2C%20Virginia%20Beach%2C%20VA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-76.12085270996091%2C%22east%22%3A-75.9715073120117%2C%22south%22%3A36.823989603669176%2C%22north%22%3A36.9385050158866%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A246020%2C%22regionType%22%3A8%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A700000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3149%7D%2C%22sqft%22%3A%7B%22min%22%3A2000%7D%2C%22doz%22%3A%7B%22value%22%3A%221%22%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D'
FORM_URL = 'https://forms.gle/tAFGECYryWTuvxjH9'
CHROME_DRIVER_PATH = 'C:\\Users\\alaliashvili\\Development\\chromedriver'

## collect housing data
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

response = requests.get(ZILLOW_URL, headers=HEADERS)
zillow_webpage = response.text

soup = BeautifulSoup(zillow_webpage, 'html.parser')

links = soup.select(selector='div.list-card-info a')
addresses = soup.find_all(name='address', class_='list-card-addr')
prices = soup.find_all(name='div', class_='list-card-price')

## write to Google Sheets
for x in range(len(addresses)):
    driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
    driver.get(FORM_URL)
    time.sleep(2)

    address = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(addresses[x].get_text())

    price = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(prices[x].get_text())

    link = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[x]['href'])

    driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    driver.quit()