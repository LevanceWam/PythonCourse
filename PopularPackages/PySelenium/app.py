# browser automation
from selenium import webdriver
import config

browser = webdriver.Chrome()
browser.get("https:/github.com")

sigin_link = browser.find_element_by_link_text("Sign in")
sigin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys(config.username)
password_box = browser.find_element_by_id("password")
password_box.send_keys(config.password)
password_box.submit()

assert config.username in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert config.username in link_label


# browser.quit()
