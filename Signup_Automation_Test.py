import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from OrangeHRM.read_gmail import get_latest_otp
driver = webdriver.Chrome()
driver.get("https://authorized-partner.vercel.app/")

wait = WebDriverWait(driver, 10)

login = driver.find_element(By.XPATH, "//a[@class='px-4 flex items-center gap-2']")
login.click()

time.sleep(3)

signup= wait.until(
    EC.element_to_be_clickable(
     (By.XPATH, "//a[normalize-space()='Sign Up']")))
signup.click()

time.sleep(3)

Agree = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@id='remember']")))
Agree.click()

time.sleep(3)

Continue = driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")
Continue.click()

time.sleep(2)

firstname = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your First Name']").send_keys("Rubina")
lastname = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Last Name']").send_keys("Adhikari")
email = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Email Address']").send_keys("adhikarirubina160@gmail.com")
phone = driver.find_element(By.XPATH, "//input[@placeholder='00-00000000']").send_keys("9761658229")
password = driver.find_element(By.XPATH, "//input[@placeholder='******************']").send_keys("Helloworld1@")
confirmpassword = driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys("Helloworld1@")

# Record the time before clicking Next
request_started_at = int(time.time() * 1000)

# Click Next
driver.find_element(
    By.XPATH, "//button[normalize-space()='Next']"
).click()

print("Next button clicked. Waiting for OTP...")

# Wait for OTP input field
otp_input = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'input[data-input-otp="true"]')
    )
)

print("OTP input field is visible.")

# Get the latest OTP from Gmail
otp = get_latest_otp(request_started_at)
print("OTP received:", otp)
print("New OTP received from Gmail.")

# Enter OTP into website
otp_input.send_keys(otp)

print("OTP entered successfully.")

# Click Verify Code
verify_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Verify Code']")
    )
)

verify_button.click()

print("Verify Code button clicked.")

verify_code = driver.find_element(By.XPATH, "//button[normalize-space()='Verify Code']").click()
time.sleep(1)

