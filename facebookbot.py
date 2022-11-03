from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
from random import randint

class FacebookBot:
    drive = None

    def __init__(self, driver):
        self.driver = driver


    def login(self, username, password):
        self.driver.get("https://mbasic.facebook.com")

        # Login to facebook
        print("Logging into facebook...")
        usr_elem = self.driver.find_element_by_css_selector('#m_login_email')
        pwd_elem = self.driver.find_element_by_css_selector(
            '#password_input_with_placeholder > input'
        )

        usr_elem.send_keys(username)
        pwd_elem.send_keys(password)
        pwd_elem.send_keys(Keys.RETURN)
        time.sleep(2)  # We'll wait 2 seconds for the page to load completely.


    def post_to_groups(self, post, groups):
        # Go to each group and post
        for i, group in enumerate(groups):
            self.driver.get(group)
            time.sleep(3)

            try:
                # Encontra e salva o nome da cidade.
                page = self.driver.page_source
                soup = BeautifulSoup(page, 'html.parser')
                results = soup.find(id='objects_container')
                city_name = results.find('div', class_='bp')

                # Encontra o campo de postagem e o botão publicar.
                post_elem = self.driver.find_element(By.NAME, 'xc_message')
                sub_elem = self.driver.find_element(By.NAME, 'view_post')

                # Escreve no campo postagem e clica em publicar.
                post_elem.send_keys(post)
                time.sleep(1)
                sub_elem.click()

                # Informa se tudo deu certo, o nome do grupo e o link.
                print(f'Sucessfully posted in group #{i}: {city_name.text}.')
                print(f'Link: {group}.\n')

                random_sleep = randint(10, 60)
                time.sleep(random_sleep)
            except NoSuchElementException:
                print(f"Can't post in group {city_name}.\nLink: {group}.")
