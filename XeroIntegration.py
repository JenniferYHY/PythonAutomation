# from selenium import time
# from selenium.common.exceptions import TimeoutException
#from Try_package.Features.signup import signup
from Try_package.Features.Login import login

#signup()

def setup_xero_integration ():
    
    driver = login()
    login()

    
    menu = driver.find_element_by_xpath("//*[@id=\"main-nav\"]/div[1]/ul/li[8]/a/span[1]")
    
    menu.click()
    
    
if __name__ == "__main__":
    setup_xero_integration()