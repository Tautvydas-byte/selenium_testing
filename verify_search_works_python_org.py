import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import timedelta

driver = webdriver.Chrome(executable_path="/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver")

driver.get('https://python.org/')
driver.implicitly_wait(10)  # 10 sec until it say element npt found

search_field_id = "id-search-field"
search_field_elm = driver.find_element(By.ID, search_field_id)
search_field_elm.send_keys("testing")

go_btn_id = "submit"
go_btn_id = driver.find_element(By.ID, go_btn_id)
go_btn_id.click()

first_result_xpath = '//*[@id="content"]/div/section/form/ul/li[1]'
first_result_elm = driver.find_element(By.XPATH, first_result_xpath)
# import pdb; pdb.set_trace()
# assert first_result_elm.is_displayed(), f"After searching the result is not displayed"

if first_result_elm.is_displayed():
    print("Element is displayed - PASS")
else:
    driver.save_screenshot("Not_displayed.png");
    raise Exception(f"After searching the result is not displayed")

# driver.quit()
