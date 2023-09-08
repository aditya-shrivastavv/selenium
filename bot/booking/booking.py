from selenium import webdriver
import os
import booking.constants as const
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"E:/Drivers/SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__(options=options)

    def __exit__(self, exc_type, exc_val, traceback):
        """Automatically executes after the execution of the context manager has finished."""
        self.quit()

    def launch_website(self):
        self.get(const.BASE_URL)
        self.maximize_window()
