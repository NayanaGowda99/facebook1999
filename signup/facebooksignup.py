from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path=r"C:\Users\ADMIN\Downloads\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(path)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)
#create new account
driver.find_element("link text","Create New Account").click()
#first name textfield
driver.find_element("xpath","//input[@name='firstname']").send_keys("Parignya")
#surname textfield
driver.find_element('''xpath''','''//input[@name="lastname"]''').send_keys("gowda")
#emailid or mobile no textfield
driver.find_element('''xpath''','''//input[@name="reg_email__"]''').send_keys(r"parignya1999@gmail.com")
#confirm emailid textfield
driver.find_element('''xpath''','''//input[@name="reg_email_confirmation__"]''').send_keys(r"parignya1999@gmail.com")
#new password textfield
driver.find_element('''xpath''','''//input[@name="reg_passwd__"]''').send_keys("Sumithra@1999")
#select date dropdown
dt = driver.find_element("id","day")
sel_dt = Select(dt)
sel_dt.select_by_visible_text('13')

#select month dropdown
mon = driver.find_element("id","month")
sel_mon = Select(mon)
sel_mon.select_by_visible_text('Mar')

#select year dropdown
yr = driver.find_element("id","year")
sel_yr = Select(yr)
sel_yr.select_by_visible_text('1999')

#select gender radio button
driver.find_element("xpath","//label[@class='_58mt']/..//input[@class='_8esa'][1]").click()

#signup button
driver.find_element("name","websubmit").click()


driver.refresh()
#username textfield
driver.find_element("xpath","//input[@name='email']").send_keys("kmaadhya2727@gmail.com")
#password textfield
driver.find_element("xpath","//input[@name='pass' or @id='pass']").send_keys("Sumithra@1999")
#login button
driver.find_element("xpath","//button[@name='login']").click()
time.sleep(2)
driver.close()


