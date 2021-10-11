from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_name(browser):
    browser.get("http://localhost")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1 > a")), message='')
    assert el.text == "Your Store"


def test_check_cart(browser):
    browser.get("http://localhost")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "cart-total")), message='')


def test_check_macbook(browser):
    browser.get("http://localhost")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-layout:nth-child(1) .caption a")), message='')
    assert el.text == "MacBook"


def test_check_serch(browser):
    browser.get("http://localhost")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control")), message='')


def test_check_serch(browser):
    browser.get("http://localhost")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-layout:nth-child(4) button:nth-child(2)")), message='')
