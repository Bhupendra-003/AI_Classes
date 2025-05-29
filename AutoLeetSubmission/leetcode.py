from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
import time

# Path to Brave browser binary
brave_path = "/usr/bin/brave-browser"

# Set up options
options = Options()
options.binary_location = brave_path

# Optional: run in headless mode
# options.add_argument('--headless')

# Create WebDriver with ChromeDriver
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Navigate to leetcode.com so domain matches for cookies
driver.get("https://leetcode.com")
time.sleep(5)  # Let it load fully

# Step 2: Load cookies
with open("Python/Module1/leetcode_cookies.pkl", "rb") as f:
    cookies = pickle.load(f)
    for cookie in cookies:
        if 'sameSite' in cookie:
            del cookie['sameSite']  # Optional fix for Selenium quirks
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print("Failed to add cookie:", e)

# Step 3: Reload the problem page after adding cookies
driver.get("https://leetcode.com/problems/median-of-two-sorted-arrays/description/")
time.sleep(10)

# Step 4: Click the button
button = driver.find_element(By.CSS_SELECTOR, '[data-e2e-locator="console-submit-button"]')
button.click()
