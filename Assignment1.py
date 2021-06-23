from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

import time
driver= Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element_by_xpath("//input[contains(@id,'twotabsearchtextbox')]").send_keys("iphone 11(64Gb) ")
driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()
driver.find_element_by_xpath("//span[text()='Apple']").click()
driver.find_element_by_xpath("//span[text()='64 GB']").click()
phones=driver.find_elements_by_xpath("//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
prices=driver.find_elements_by_xpath("//span[contains(@class,'a-price-whole')]")

for phone in phones:
    print(phone.text)
for price in prices:
    print(price.text)
time.sleep(5)
#driver.quit()
