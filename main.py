import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# setting an environment variable in system for the runtime
os.environ["PATH"] += r"E:/Drivers/SeleniumDrivers"

# workaround to make the browser stay open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)


def main():
    driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

    # Wait for the website to load properly, wait 3 secs.
    driver.implicitly_wait(10)

    downloadBtn = driver.find_element(By.ID, "downloadButton")
    downloadBtn.click()

    # Explicit wait untill the progress is completed.
    WebDriverWait(driver=driver, timeout=30).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "progress-label"),  # Getting the element
            "Complete!",  # Expected text
        )
    )


main()
