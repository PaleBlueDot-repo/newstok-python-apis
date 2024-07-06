import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

newspaper_base_url = 'https://www.bangla.24livenewspaper.com/'

def contains_url(text):
    url = "https://www.bangla.24livenewspaper.com/post-"
    return url in text

def scrape_bangla_news(topic, max_pages_index):
    output_result = []
    index = 1

    # Setup Selenium with ChromeDriverManager
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run headless Chrome
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    while index<=max_pages_index:
        url = f'{newspaper_base_url}{topic}?start={index}'
        print("Fetching URL:", url)
        
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//h2/a'))
            )
        except:
            print(index)
            index+=1
            continue

        # Find all <h2> tags with class 'item-title'
        h2_tags = driver.find_elements(By.XPATH, '//h2/a')
        print(f"Found {len(h2_tags)} <h2> tags with class 'item-title'")
        news_info = []
        for h2_tag in h2_tags:
            title = h2_tag.text
            link = h2_tag.get_attribute('href')
            if(contains_url(link)):
                news_info.append({'title': title, 'link': link})
        for news in news_info:
            url = news['link']
            if(url):
                driver.get(url)
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@class='item-page']/div/p"))
                    )
                except:
                    print("line 57---------- not found")
                    continue

                # Find the elements
                article_elements = driver.find_elements(By.XPATH, "//div[@class='item-page']/div/p")

                # Extract the text from each element and combine into a single string
                article_texts = [element.text for element in article_elements]
                article = " ".join(article_texts)

                time_elements = driver.find_element(By.XPATH, "//*[@class='published']/time")

                # Extract the datetime attribute from each element
                datetimes = time_elements.get_attribute('datetime')
                output_result.append({'title': news['title'], 'link': news['link'], 'article': article, 'published': datetimes})

        
        index += 1  # Increment index to fetch the next set of articles

    driver.quit()
    return output_result