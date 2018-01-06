from selenium import webdriver
from facebookbot import FacebookBot

usr = input('Username: ')
pwd = input('Password: ')

# Initiate webdriver - PhantomJS
print("Iniatiating PhantomJS")
driver = webdriver.PhantomJS()

myBot = new FacebookBot(driver)
myBot.login(usr, pwd)

groups = myBot.collectGroups()

post = """ Sample Post """ # change this to what you will post to each group
myBot.postToGroups(post, 500, groups)
