# pip install selenium
# pip install python-dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

browser = webdriver.Firefox()
browser.get("https://ead.especializati.com.br")
username_input = browser.find_element(By.NAME, "email")
username_input.send_keys(username)
password_input = browser.find_element(By.NAME, "password")
password_input.send_keys(password)

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.submit()
