import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

#open chrome and maximize window
driver = webdriver.Chrome()
driver.maximize_window()
sleep(0.75)

#go to google images
driver.get("https://www.google.com/imghp?hl=en")
sleep(0.75)

#accept cookies
cookies = driver.find_element(By.ID, "L2AGLb")
cookies.click()
sleep(0.75)

#finds the search bar and search for Peter Griffin
text_area = driver.find_element(By.NAME, "q")
text_area.clear()
text_area.send_keys("Peter Griffin")
sleep(0.75)
text_area.send_keys(Keys.RETURN)

#finds the first image
sleep(0.75)
first_image = driver.find_element(By.PARTIAL_LINK_TEXT, "data:image/jpeg;base64,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")
first_image.contextClick()
sleep(0.75)

#downloads it

sleep(5)
