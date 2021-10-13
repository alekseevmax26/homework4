from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_desktops(browser):
    browser.get("http://localhost")
    click_desktops = browser.find_element_by_xpath("//a[contains(text(),'Desktops')]")
    click_desktops.click()
    click_mak = browser.find_element_by_xpath("//a[contains(text(),'Mac (1)')]")
    click_mak.click()
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Mac"


def test_check_components(browser):
    browser.get("http://localhost")
    click_components = browser.find_element_by_xpath("//a[contains(text(),'Components')]")
    click_components.click()
    click_monitors = browser.find_element_by_xpath("//a[contains(text(),'Monitors (2)')]")
    click_monitors.click()
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Monitors"


def test_check_tablets(browser):
    browser.get("http://localhost")
    click_tablets = browser.find_element_by_xpath("//a[contains(text(),'Tablets')]")
    click_tablets.click()
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Tablets"


def test_check_software(browser):
    browser.get("http://localhost")
    click_software = browser.find_element_by_xpath("//a[contains(text(),'Software')]")
    click_software.click()
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Software"


def test_check_phones(browser):
    browser.get("http://localhost")
    click_phones = browser.find_element_by_xpath("//a[contains(text(),'Phones & PDAs')]")
    click_phones.click()
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Phones & PDAs"
