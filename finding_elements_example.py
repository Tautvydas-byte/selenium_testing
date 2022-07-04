from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pdb  # python debbuging

driver = webdriver.Chrome(executable_path="/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver")

driver.get('http://demostore.supersqa.com')

# finding elements By.ID
cart = driver.find_element(By.ID, "site-header-cart")
#print(cart)
#print(type(cart))
#cart_text = cart.text
#print(cart_text)

search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('Hoodie')
search_field.send_keys(Keys.ENTER)

# By.CSS_SELECTOR
# my_account = driver.find_element(By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9")
# my_account = driver.find_element(By.XPATH, "//*[@id="site-navigation"]/div[1]/ul/li[4]")#xpath
#my_account = driver.find_element(By.XPATH, "/html/body/div/header/div[2]/div/nav/div[1]/ul/li[4]")  # full xpath
#my_account.click()

#pdb.set_trace()

# driver.quit()  # close chrome
# driver.close()  # close active tab
