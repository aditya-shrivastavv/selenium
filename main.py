import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# setting an environment variable in system for the runtime
os.environ["PATH"] += r"E:/Drivers/SeleniumDrivers"

# workaround to make the browser stay open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)


def main():
    driver.get("https://www.rapidtables.com/calc/math/Add_Calculator.html")

    driver.implicitly_wait(5)

    inputField1 = driver.find_element(By.NAME, "x")
    inputField2 = driver.find_element(By.NAME, "x2")
    submitButton = driver.find_element(By.XPATH, "//input[@onclick='calc3()']")
    outputField = driver.find_element(By.ID, "y")

    try:
        captchCloseBtn = driver.find_element(By.XPATH, "//span[@aria-hidden='true']")
        captchCloseBtn.click()
    except:
        print("No Captcha")

    inputField1.clear()
    inputField1.send_keys(99)

    inputField2.clear()
    inputField2.send_keys(99)

    # submitButton.click()
    submitButton.send_keys(Keys.ENTER)

    result = outputField.get_attribute("value")
    print("Result:", result)


main()
