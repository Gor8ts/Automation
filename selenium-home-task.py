from selenium import webdriver

driver = webdriver.Firefox()
driver.get ("https://www.selenium.dev")

title = driver.title
print(title)
driver.quit()