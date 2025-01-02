#!/usr/bin/python3
# author: jithuantony4u@gmail.com
# description: this python script will help to do sanity test using selenium webdriver

from selenium import webdriver

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

def main():
    driver = get_driver()
    try:
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
        if element.text:
            return f"Message retrieved successfully: {element.text}"
        else:
            return "Failed to retrieve the message."
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        driver.quit()

if __name__ == "__main__":
    print(main())
