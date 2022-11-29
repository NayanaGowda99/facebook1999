import re
from selenium import webdriver
# path = r"C:\Users\ADMIN\Downloads\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
from selenium.webdriver.support.select import Select
from LIBRARY.config import Config
import time
from DATA.reading_objects import ReadExcel
read_xl=ReadExcel()

login_obj=read_xl.read_locators(Config.read_locators)
print(login_obj)
# driver.get("https://www.facebook.com/")
class Facebook:
    def __init__(self,driver):
        self.driver=driver

    def Createnewaccount(self):
        #self.driver.find_element('link text', 'Create New Account').click()
        self.driver.find_element(*login_obj["click_button1"]).click()
        time.sleep(2)

    def firstname(self,firstname_value):
        self.driver.find_element(*login_obj["txt_firstname"]).send_keys(firstname_value)


    def surname(self,surname_value):
        self.driver.find_element(*login_obj["txt_surname"]).send_keys(surname_value)


    def emailid(self,email_id):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email_id)
        assert result, "invalid email"
        self.driver.find_element(*login_obj["txt_emailid1"]).send_keys(email_id)


    def con_emailid(self,conemail_id):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, conemail_id)
        assert result, "invalid email"
        self.driver.find_element(*login_obj["txt_emailid2"]).send_keys(conemail_id)


    def new_password(self,newpassword_value):
        if isinstance(newpassword_value, float):
            pwd = str(int(newpassword_value))
        assert len(newpassword_value) >= 6, "password should have atleast 6 characters"
        self.driver.find_element(*login_obj["txt_newpassword"]).send_keys(newpassword_value)

    def date(self):
        dt = self.driver.find_element(*login_obj["txt_select_date"])
        sel_dt = Select(dt)
        sel_dt.select_by_visible_text('13')

    def month(self):
        mon = self.driver.find_element(*login_obj["txt_select_month"])
        sel_mon = Select(mon)
        sel_mon.select_by_visible_text('Mar')

    def year(self):
        yr = self.driver.find_element(*login_obj["txt_select_year"])
        sel_yr = Select(yr)
        sel_yr.select_by_visible_text('1999')

    def gender(self):
        self.driver.find_element(*login_obj["click_gender_button"]).click()

    def signup(self):
        self.driver.find_element(*login_obj["click_button"]).click()
        self.driver.refresh()
        time.sleep(2)

    def username(self,username_value):

        self.driver.find_element(*login_obj["txt_username"]).send_keys(username_value)

    def password(self,password_value):
        self.driver.find_element(*login_obj["txt_password"]).send_keys(password_value)

    def login(self):
        self.driver.find_element(*login_obj["click_button2"]).click()
        time.sleep(2)

    def close(self):
        self.driver.close()

# lp=Facebook(driver)
# lp.Createnewaccount()
# lp.firstname()
# lp.surname()
# lp.emailid()
# lp.con_emailid()
# lp.new_password()
# lp.date()
# lp.month()
# lp.year()
# lp.gender()
# lp.signup()
# lp.username()
# lp.password()
# lp.login()
# lp.close()
