from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import booking.constants as const

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"E:/Drivers/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path

        # Decides whether to close the browser window automatically after running the context manager.
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, traceback):
        """Automatically executes after the execution of the context manager has finished."""
        if self.teardown:
            self.quit()

    def launch_website(self):
        self.get(const.BASE_URL)

    def close_popup(self):
        try:
            popupCloseBtn = self.find_element(
                By.XPATH, '//button[@aria-label="Dismiss sign-in info."]'
            )
            popupCloseBtn.click()
        except:
            print("No Popup?")
            pass

    def change_currency(self, currency=None):
        pass

    def destination(self, place):
        placeField = self.find_element(By.NAME, "ss")
        placeField.clear()
        placeField.send_keys(place)
        placeField.send_keys(Keys.ARROW_DOWN)
        placeField.send_keys(Keys.ENTER)

    def selectDates(self, checkin=None, checkout=None):
        checkinDate = self.find_element(By.CSS_SELECTOR, f'span[data-date="{checkin}"]')
        checkinDate.click()
        checkoutDate = self.find_element(By.CSS_SELECTOR, f'span[data-date="{checkout}"]')
        checkoutDate.click()

    def selectAdults(self, count=1):
        selectElement = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        selectElement.click()

        # decreaseAdult = self.find_element()
