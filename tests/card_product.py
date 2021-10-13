from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_name(browser):
    browser.get("http://localhost/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p:nth-child(1) > b")), message='')
    assert el.text == "Intel Core 2 Duo processor"


def test_check_price(browser):
    browser.get("http://localhost/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2:nth-child(1)")), message='')
    assert el.text == "$602.00"


def test_check_cart(browser):
    browser.get("http://localhost/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.ID, "button-cart")), message='')
    assert el.text == "Add to Cart"


def test_check_reviews(browser):
    browser.get("http://localhost/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a:nth-child(6)")), message='')
    assert el.text == "0 reviews"


def test_check_reviews_write(browser):
    browser.get("http://localhost/index.php?route=product/product&product_id=43")
    click_reviews = browser.find_element_by_css_selector("a:nth-child(6)")
    click_reviews.click()
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2:nth-child(2)")), message='')
    assert el.text == "Write a review"
