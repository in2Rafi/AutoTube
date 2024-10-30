from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

login_upload_url = "https://rumble.com/login.php?next=%2Fupload.php"
username = "un"
password = "pw"


try:
    #Browse the upload page. We have to login first. Afterwords the link will take us to the upload page
    driver.get(login_upload_url)
    time.sleep(10)
    
    #Input username
    username_field = driver.find_element(By.ID, "login-username")
    username_field.send_keys(username)
    
    #Input password
    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys(password)
    time.sleep(10)
    
    #lets login
    login_button = driver.find_element(By.XPATH, '//button[text()="Sign in"]')
    login_button.click()
finally:
    print("done")