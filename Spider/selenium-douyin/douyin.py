import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.douyin.com/user/MS4wLjABAAAA2JmxeROm5PsNNZ7H1_1U5ek97hQAXxZzbYWUxWMheVs?vid=7183677806222609679'

chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument(
    'user-agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
wait = WebDriverWait(driver, 50)

close_p = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dy-account-close')))
close = driver.find_element(By.CLASS_NAME, 'dy-account-close')
close.click()
for i in range(18):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
