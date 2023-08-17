from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get ("https://www.google.com")

elem = driver.find_element(By.NAME,"q")
elem.send_keys("Hello WebDriver")
elem.submit()

print(driver.title)
driver.quit()