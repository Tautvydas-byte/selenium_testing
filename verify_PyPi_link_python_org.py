import self
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver")

driver.get('https://python.org/')

current_title = driver.title
expected_title = 'Welcome to Python.org'

if current_title != expected_title:
    raise Exception(f"Went to python.org but got wrong title. Current title: {current_title}")
else:
    print("Title is correct - PASS")
# ---------------------------------------------------------------------
# PyPi headeryje paspaudzia nuoroda/mygtuka
pypi_header_link_locator = '#top > nav > ul > li.pypi-meta > a'
pypi_header_link_elm = driver.find_element(By.CSS_SELECTOR, pypi_header_link_locator)
pypi_header_link_elm.click()

cur_url = driver.current_url
expected_url = 'https://Delfi.lt/'
if cur_url != expected_url:
    driver.save_screenshot("Wrong_URL.png")
    raise Exception(f"Went to {expected_url} but got wrong url. Current url: {cur_url}")
else:
    print("URL is correct - PASS")
# driver.quit()
