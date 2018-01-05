from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import re


# Post
post = """ Sample Post """ # change this to what you will post to each group
interval = 500 # amount of time to wait before posting to next group

# Login information for Facebook
usr = input("Username: ")
pwd = input("Password: ")

# Initiate webdriver - PhantomJS
print("Iniatiating PhantomJS")
driver = webdriver.PhantomJS()

# We'll use this url for easy element targeting
driver.get("https://mbasic.facebook.com")

# Login to facebook
print("Logging into facebook...")
usr_elem = driver.find_element_by_css_selector('#m_login_email')
pwd_elem = driver.find_element_by_css_selector(
    '#login_form > ul > li:nth-child(2) > div > input')

usr_elem.send_keys(usr)
pwd_elem.send_keys(pwd)
pwd_elem.send_keys(Keys.RETURN)
time.sleep(2)  # We'll wait 2 seconds for the page to load completely

# Collect all groups profile
print("Collecting groups in profile...")
driver.get('https://mbasic.facebook.com/groups/?seemore&refid=27')

groups = []
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")

for group in soup.find_all("a", href=re.compile(r"groups/\d")):
    groups.append("https://mbasic.facebook.com" + group['href'])

print(f"{len(groups)} groups found in profile.")

# Go to each group and post
for i, group in enumerate(groups):
    driver.get(group)
    try:
        post_elem = driver.find_element_by_css_selector('#u_0_0')
        sub_elem = driver.find_element_by_name('Post')

        post_elem.send_keys(post)
        sub_elem.click()

        print(f"Sucessfully posted in group #{i}.")
        time.sleep(interval)
    except NoSuchElementException:
        print(f"Can't post in group #{i}.")
        continue