from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver")
# driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com')
print(driver.title)