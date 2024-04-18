import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

#open chrome and maximize window
driver = webdriver.Chrome()
driver.maximize_window()
sleep(1.25)

#go to the game webiste
driver.get("https://edoardosgherri.wixstudio.io/htmlgames/blank")
sleep(2)

#go to games section
#game_section_starter = driver.find_element(By.Name, "kGvnrc")
#game_section_starter.click()
#sleep(0.75)

#finds the start button and clicks it
start_button_clicker = driver.find_element(By.CSS_SELECTOR, "#center .start")
sleep(0.25)
start_button_clicker.contextClick()
sleep(0.75)
#finds the input bar and insert words



sleep(5)