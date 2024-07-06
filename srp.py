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

def scrape_bangla_news(topic):
    output_result = []
    index = 0  # Initialize index here

    # Setup Selenium with ChromeDriverManager
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run headless Chrome
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    
    url = 'https://www.bangla.24livenewspaper.com/bangladesh?start=13'
    print("Fetching URL:", "https://www.bangla.24livenewspaper.com/bangladesh?start=13")
    
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h2/a'))
    )

    # Find all <h2> tags with class 'item-title'
    h2_tags = driver.find_elements(By.XPATH, '//h2/a')
    print(f"Found {len(h2_tags)} <h2> tags with class 'item-title'")

    for h2_tag in h2_tags:
        title = h2_tag.text
        link = h2_tag.get_attribute('href')
        output_result.append({'title': title, 'link': link})
    
    index += 10  # Increment index to fetch the next set of articles

    # driver.quit()
    return output_result

# Example usage
topic = 'category/news'  # Replace with the desired topic path
results = scrape_bangla_news(topic)
print(json.dumps(results, ensure_ascii=False, indent=2))
