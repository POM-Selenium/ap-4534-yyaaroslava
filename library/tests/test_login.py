from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login(driver):
    driver.get("http://127.0.0.1:8000")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys("yy@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("yy")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Welcome,')]")))
    print("Login successful")


def test_logout(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
    print("Logout successful")


def test_invalid_login(driver):
    driver.get("http://127.0.0.1:8000/auth/login/")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys("wrong@wrong.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "text-danger")))
    print("Invalid login test passed")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        test_valid_login(driver)
        test_logout(driver)
        test_invalid_login(driver)
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
