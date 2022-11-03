from selenium import webdriver
from facebookbot import FacebookBot

from webdriver_manager.chrome import ChromeDriverManager

usr = str(input('User: '))
pwd = str(input('Password: '))

# Initiate webdriver.
print("Iniatiating...")

#Para não abrir o navegador.
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), 
                          chrome_options=options)

myBot = FacebookBot(driver)
myBot.login(usr, pwd)
print('')

groups = [
    '', # Coloque os links dos grupos aqui.
]

post = str(input('Insert a link here: '))
print('')

myBot.post_to_groups(post, groups)
