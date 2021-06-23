from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

import time
driver= Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("//a[text()='Login']")
driver.find_element_by_xpath("//input[contains(@class,'_2IX_2- VJZDxU')]").send_keys("7842126141")
driver.find_element_by_xpath("//input[contains(@class,'_2IX_2- _3mctLh VJZDxU')]").send_keys("mxy637")
driver.find_element_by_xpath("//button[contains(@class,'_2KpZ6l _2HKlqd _3AWRsL')]").click()
driver.find_element_by_xpath("//input[@name='q']").send_keys("iphone XR")
driver.find_element_by_class_name("L0Z3Pu").click()

time.sleep(5)
#driver.quit()