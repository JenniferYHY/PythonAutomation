from selenium.webdriver.support.select import Select
from webdriver import get_webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Try_package.Features.ConfigLoader import get_signup_config
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import NoSuchElementException
# from selenium import time
# from selenium.common.exceptions import TimeoutException
def signup():
    
    config = get_signup_config()

    url = "https://{}.unleashedsoftware.com/v2/Account/Register".format(config['environment'])
    
    driver = get_webdriver()
    
    driver.get(url)
    
    firstname = driver.find_element_by_name("FirstName")
    lastname = driver.find_element_by_name("LastName")
    email = driver.find_element_by_id("Email")
    submit1 = driver.find_element_by_id("btnRegister")
    
    firstname.send_keys(config['firstname'])
    lastname.send_keys(config['lastname'])
    email.send_keys(config['email'])
    submit1.click()
    
    driver.implicitly_wait(3)
    
    company = driver.find_element_by_name("Company")
    country = Select (driver.find_element_by_name("Country"))
    state = Select (driver.find_element_by_id("State"))
    city = driver.find_element_by_name("txtCity")
    phone = driver.find_element_by_id("Phone")
    currency = Select (driver.find_element_by_id("BaseCurrencies"))
    industry = Select (driver.find_element_by_id("Industry"))
    submit2 = driver.find_element_by_id("btnRegister")
    
    
    company.send_keys(config['company'])
    country.select_by_visible_text(config['country'])    
    state.select_by_visible_text(config['state'])
    city.send_keys(config['city'])
    phone.send_keys(config['phone'])
    currency.select_by_visible_text(config['currency'])
    industry.select_by_visible_text(config['industry'])
    driver.find_element_by_xpath("//*[@id=\"inputform\"]/div/div[3]/label").click()
    submit2.click()
     
    #driver.implicitly_wait(3) 
    #WebDriverWait.until(ec.visibility_of_element_located((By.XPATH,"//*[@id=\"newPassword\"]")))
    newpassword = driver.find_element_by_id("newPassword")
    confirmPassword = driver.find_element_by_id("confirmPassword")
    activate = driver.find_element_by_id("ActivateButton")
    

    newpassword.send_keys(config['newpassword'])
    confirmPassword.send_keys(config['newpassword'])
    activate.click()
    
if __name__ == "__main__":
    signup()