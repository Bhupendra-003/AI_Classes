from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pickle
import time

# Path to your Brave browser
brave_path = "/usr/bin/brave-browser"

# Set up Chrome options for Brave
options = Options()
options.binary_location = brave_path

# Initialize the driver
driver = webdriver.Chrome(options=options)

# Open LeetCode login page
driver.get("https://leetcode.com/accounts/login/")

# Give time to login manually
print("Please log in manually in the browser window...")
time.sleep(30)  # Wait for login

# Save cookies to a file
with open("leetcode_cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Cookies saved successfully!")

driver.quit()
