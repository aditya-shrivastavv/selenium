import os
from selenium import webdriver

# setting an environment variable in system for the runtime
os.environ['PATH'] += r"E:/Drivers/SeleniumDrivers"

# workaround to make the browser stay open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

def main():
    driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
    
    # Wait for the website to load properly, wait 3 secs.
    driver.implicitly_wait(10)
    
    downloadBtn = driver.find_element("id", "downloadButton")
    downloadBtn.click()

main()