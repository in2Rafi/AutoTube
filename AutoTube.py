from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

try:
    driver.get("https://www.google.com")
finally:
    print("done")