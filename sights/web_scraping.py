from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager.install()))
browser.get("https://www.hotels.com/")

dep_input = browser.find_element(By.XPATH, "//*[@id='YkXo']/div/div/div/div[1]/div[2]/div/div[1]/div/div/input")
dep_input.send_keys("TUL")

dest_input = browser.find_element(By.XPATH, "//*[@id='YkXo']/div/div/div/div[1]/div[2]/div/div[3]/div/div/input")
dest_input.send_keys("CDG")
