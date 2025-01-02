#!/usr/bin/python3
# author: jithuantony4u@gmail.com
# description: this python script will help to do sanity test using selenium webdriver

from selenium import webdriver
import time
from datetime import datetime as dt

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    try:
        return float(text.split(": ")[1])
    except (IndexError, ValueError):
        return None  # Return None if the text cannot be parsed
    
def write_files(text):
    filename = f"{dt.now().strftime("%Y-%m-%d.%H-%M-%S")}.txt"
    with open (filename, 'w') as file:
        file.write(text)    

def main():
    driver = get_driver()
    while True:
        time.sleep(3)  # Allow time for the page to load completely
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_files(text)

if __name__ == "__main__":
    print(main())
