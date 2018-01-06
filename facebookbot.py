from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import re

class FacebookBot:
    def __init__(driver):
        self.driver = driver

    def login(username, password):
        self.driver.get("https://mbasic.facebook.com")

        # Login to facebook
        print("Logging into facebook...")
        usr_elem = self.driver.find_element_by_css_selector('#m_login_email')
        pwd_elem = self.driver.find_element_by_css_selector(
            '#login_form > ul > li:nth-child(2) > div > input')

        usr_elem.send_keys(usr)
        pwd_elem.send_keys(pwd)
        pwd_elem.send_keys(Keys.RETURN)
        time.sleep(2)  # We'll wait 2 seconds for the page to load completely

    def collectGroups():
        print("Collecting groups in profile...")
        self.driver.get('https://mbasic.facebook.com/groups/?seemore&refid=27')

        groups = []
        source = self.driver.page_source
        soup = BeautifulSoup(source, "html.parser")

        for group in soup.find_all("a", href=re.compile(r"groups/\d")):
            groups.append("https://mbasic.facebook.com" + group['href'])

        print(f"{len(groups)} groups found in profile.")

        return groups

    def postToGroups(post, interval, groups):
        # Go to each group and post
        for i, group in enumerate(groups):
            self.driver.get(group)
            try:
                post_elem = self.driver.find_element_by_css_selector('#u_0_0')
                sub_elem = self.driver.find_element_by_name('Post')

                post_elem.send_keys(post)
                sub_elem.click()

                print(f"Sucessfully posted in group #{i}.")
                time.sleep(interval)
            except NoSuchElementException:
                print(f"Can't post in group #{i}.")
                continue
