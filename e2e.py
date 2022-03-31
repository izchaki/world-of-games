from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
chromeOptions.headless = True
chrome_driver = webdriver.Chrome(options=chromeOptions)


def test_scores_service(url):
    try:
        chrome_driver.get(url)
        scores = chrome_driver.find_element(By.XPATH, value='//*[@id="score"]').text
        print(scores)
        chrome_driver.quit()
        return 1 < int(scores) < 1000
    except Exception as e:
        print(e)


def main_function():
    if test_scores_service('http://localhost:5001') is True:
        return 0
    return -1

time.sleep(5)
print(main_function())
