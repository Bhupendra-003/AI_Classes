# 🚀 LeetCode Automation with Selenium & Brave

This project automates interaction with LeetCode problems using Selenium and the Brave browser. It allows you to log in with saved cookies and simulate actions like submitting a solution.


---

## 📦 Requirements

- Python 3.10+
- Brave browser
- ChromeDriver (compatible with your Brave version)
- Selenium Python library

---

## ⚙️ Setup Instructions

### 1. ✅ Install Python Dependencies

```bash
pip install selenium
```

## 🍪 Usage

### 1. Get Cookies

- Run `getCookies.py`. This script will open a Brave browser window and navigate to the LeetCode login page.
- Manually log in to your LeetCode account in the browser.
- The script will wait for 30 seconds to allow you to log in.
- After successful login, the script saves your cookies to `leetcode_cookies.pkl`.

### 2. Automate LeetCode Submission

- Ensure that you have a solution ready for the LeetCode problem you want to submit.
- Modify the `leetcode.py` script to navigate to the specific problem URL.
- Run `leetcode.py`. This script will:
    - Open a Brave browser instance.
    - Load the cookies saved in the previous step.
    - Navigate to the specified LeetCode problem page.
    - Locate and click the submit button.

**Note:** You may need to adjust the sleep times in the scripts to accommodate slower internet connections or page load times.

---

## ⚠️ Important Considerations

- **ChromeDriver Version:** Ensure that the ChromeDriver version matches your Brave browser version to avoid compatibility issues.
- **Cookie Expiry:** LeetCode cookies may expire after a certain period. If the automation stops working, you may need to regenerate the cookies using `getCookies.py`.
- **LeetCode's Terms of Service:** Be aware of LeetCode's terms of service regarding automation. Avoid excessive submissions or any activity that could be considered abusive.

---

## 📝 Disclaimer

This project is intended for educational purposes only. Use it responsibly and at your own risk, this might ban your leetcode account.


