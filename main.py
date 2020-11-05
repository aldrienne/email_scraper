"""
Author: Aldrienne Janne Maniti
Description: Download emails from gmail
"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(email,password):
    try:
        email_container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='identifier']"))
        )

        email_field = driver.find_element_by_css_selector("input[name='identifier']")
        email_field.send_keys(email_address)
        email_field.send_keys(Keys.RETURN)

        password_container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
        )

        pass_field = driver.find_element_by_css_selector("input[name='password']")
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    login_link = "https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    email_address = 'myEmail'
    password = "myPassword"

    # STEP 1 LOCATE CHROME DRIVER
    PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
    # STEP 2 SPECIFY BROWSER DRIVER
    driver = webdriver.Chrome(PATH)
    # STEP 3 ACCESS URL
    driver.get(login_link)

    # STEP 4 LOGIN to GMAIL
    login(email_address,password)




