from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_name(browser):
    browser.get("http://localhost/admin/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img")), message='')


def test_check_username(browser):
    browser.get("http://localhost/admin/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-username")), message='')


def test_check_password(browser):
    browser.get("http://localhost/admin/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")), message='')


def test_check_login(browser):
    browser.get("http://localhost/admin/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn")), message='')
    assert el.text == "Login"


def test_check_panel(browser):
    browser.get("http://localhost/admin/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-title")), message='')
    assert el.text == "Please enter your login details."
