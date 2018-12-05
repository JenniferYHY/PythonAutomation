'''
Created on Nov 29, 2018

@author: jennifer
'''

from webdriver import get_webdriver
from Try_package.Features.ConfigLoader import get_login_config

# from selenium import time
# from selenium.common.exceptions import TimeoutException
def login():
    config = get_login_config()
    
    url = "https://{}.unleashedsoftware.com/v2/Account/LogOn/".format(config['env'])
    
    driver = get_webdriver()
    
    driver.get(url)
    
    driver.set_page_load_timeout(5)
    
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_id("btnLogOn")
    
    username.send_keys(config['username'])
    password.send_keys(config['password'])
    submit.click()

if __name__ == "__main__":
    login()


