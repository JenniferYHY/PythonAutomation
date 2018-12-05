import configparser

def get_login_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config["LOGIN"]

def get_web_driver_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config["WEBDRIVER"]

def get_signup_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config["SIGNUP"]