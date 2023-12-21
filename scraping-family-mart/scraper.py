import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time



def get_soup(url, load_sleep_time, scroll_sleep_time):

    # Set up the driver to use a headless Chrome browser
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # Load the URL in the browser and wait for the page to load
    driver.get(url)
    driver.implicitly_wait(load_sleep_time)

    # Scroll down the page to load more jobs (repeat this several times)
    for i in range(10):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_sleep_time)

    # Extract the HTML content from the fully rendered page
    html_content = driver.page_source
    driver.quit()

    # Parse the HTML content (of the searching_page) using BeautifulSoup
    html_content = BeautifulSoup(html_content, 'html.parser')

    return html_content


url = "https://shopeefood.vn/ho-chi-minh/familymart-le-van-sy"
soup = get_soup(url=url, load_sleep_time=10, scroll_sleep_time=1)
print(soup.text)


print(soup.prettify())





target_divs = soup.find('div', class_="menu-group")
len(target_divs)

<div class="menu-group" id="section-group-menu--1" style="height: 56px; left: 0px; position: absolute; top: 0px; width: 100%;"><div class="title-menu">Món Đang Giảm</div></div>




import requests
from bs4 import BeautifulSoup


# Make an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now 'soup' is a BeautifulSoup object that you can use to navigate and manipulate the HTML

    # Example: find the title tag
    title_tag = soup.find('title')

    # Print the result
    print(title_tag.text if title_tag else "Title tag not found")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
#argument for incognito Chrome
option = Options()
option.add_argument("--incognito")
browser = webdriver.Chrome(options=option)
browser.get(url=url)
# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='c16H9d']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
soup = BeautifulSoup(browser.page_source, "html.parser")
product_items = soup.find_all("div", attrs={"data-qa-locator": "product-item"})
for item in product_items:
    item_url = f"https:{item.find('a')['href']}"
    print(item_url)
    browser.get(item_url)
    item_soup = BeautifulSoup(browser.page_source, "html.parser")
    # Use the item_soup to find details about the item from its url.
    container = item_soup.find_all("div",attrs={"id":"container"})
    for items in container:
        title = items.find("div",{"class":"pdp-product-title"})
        print(title)
browser.quit()