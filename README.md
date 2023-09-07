# Selenium

## Methods

### Implicit Wait and Explict Wait

#### Implict

```py
driver.implicitly_wait(10)
```

Sets a sticky timeout to implicitly wait for an element to be found, or a command to complete. This method only needs to be called one time per session.

#### Explicit

```py
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver=driver, timeout=30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"),  # Getting the element
        "Complete!",  # Expected text
    )
)
```

#### Implicit Wait VS Explicit Wait

- We can use implicit wait to find elements in the page
- We can use explicit wait to wait for some time untill some condition is met

## Real Life Automation Example

- When you get an OTP for something, that OTP automatically gets detected and filled into the fields and submits
