from selenium import webdriver
from Try_package.Features.ConfigLoader import get_web_driver_config

def get_webdriver():
    config = get_web_driver_config()
    if (config['web_driver_type'] == "chrome"):
        driver = webdriver.Chrome(executable_path=config['web_driver_path'])
    else:
        print("No other webdriver right now!")
        driver = webdriver.Chrome(executable_path=config['web_driver_path'])
        
    return driver