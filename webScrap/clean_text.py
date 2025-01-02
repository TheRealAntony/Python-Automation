#!/usr/bin/python3
# author: jithuantony4u@gmail.com
# description: this python script will help to do sanity test using selenium webdriver

from selenium import webdriver
import time

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

def main():
    driver = get_driver()
    time.sleep(3)  # Allow time for the page to load completely
    try:
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        if element.text:
            cleaned_text = clean_text(element.text)
            if cleaned_text is not None:
                return f"Message retrieved successfully: {cleaned_text}"
            else:
                return "Failed to parse the retrieved message."
        else:
            return "Failed to retrieve the message."
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        driver.quit()

if __name__ == "__main__":
    print(main())
