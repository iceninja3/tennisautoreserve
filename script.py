from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta

# Function to reserve a court
def reserve_court():
    # Set up the WebDriver
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
    driver.get("URL_OF_THE_TENNIS_COURT_RESERVATION_SITE")

    # Authenticate
    username = driver.find_element(By.NAME, "username")  # Adjust selector as needed
    password = driver.find_element(By.NAME, "password")  # Adjust selector as needed
    username.send_keys("YOUR_USERNAME")
    password.send_keys("YOUR_PASSWORD")
    password.send_keys(Keys.RETURN)

    # Wait for login to complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "element_after_login")))  # Adjust as needed

    # Navigate to the reservation page
    driver.get("URL_OF_THE_RESERVATION_PAGE")

    # Wait for the reservation time
    target_time = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)  # Tuesday 6 PM
    if target_time < datetime.now():
        target_time += timedelta(days=7)  # Move to next week if the time has passed

    time_to_wait = (target_time - datetime.now()).total_seconds()
    time.sleep(time_to_wait)

    # Click the buttons to reserve the court
    reserve_button = driver.find_element(By.ID, "reserve_button_id")  # Adjust selector as needed
    reserve_button.click()

    # Additional steps to complete the reservation
    # ...

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    reserve_court()
