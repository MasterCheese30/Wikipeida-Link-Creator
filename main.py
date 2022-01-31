from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Tacko_Fall")

whole_text = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]')

paragraphs = whole_text.find_elements(By.TAG_NAME, "p")
for p in paragraphs:
  links = p.find_elements(By.TAG_NAME, "a")
  for a in links:
    what_to_click = a.get_attribute("href")
    print(what_to_click)
    #driver.get(what_to_click)
    #driver.switch_to.window(driver.window_handles[0])

