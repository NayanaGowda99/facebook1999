import re
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select


@given(u'Open the chrome browser enter the valid URL')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\ADMIN\Downloads\chromedriver_win32\chromedriver.exe")
    context.driver.get("https://www.facebook.com/")
    context.driver.implicitly_wait(30)


@when(u'click on createnewaccount button')
def step_impl(context):
    context.driver.find_element("link text", "Create New Account").click()



@when(u'enter the first name "{firstname}"')
def step_impl(context,firstname):
    context.driver.find_element("xpath","//input[@name='firstname']").send_keys(firstname)


@when(u'enter the last name "{lastname}"')
def step_impl(context,lastname):
   context.driver.find_element('''xpath''', '''//input[@name="lastname"]''').send_keys(lastname)


@when(u'enter the email_id "{email_id}"')
def step_impl(context,email_id):
    pattern = r"\w+@gmail\.com"
    result = re.findall(pattern, email_id)
    assert result, "invalid email_id"
    context.driver.find_element('''xpath''', '''//input[@name="reg_email__"]''').send_keys(email_id)


@when(u're_enter the confirm_emailid "{confirm_emailid}"')
def step_impl(context,confirm_emailid):
    pattern = r"\w+@gmail\.com"
    result = re.findall(pattern, confirm_emailid)
    assert result, "invalid conform_emailid"
    context.driver.find_element('''xpath''', '''//input[@name="reg_email_confirmation__"]''').send_keys(confirm_emailid)

@when(u'enter the new password "{newpassword}"')
def step_impl(context,newpassword):
    context.driver.find_element('''xpath''', '''//input[@name="reg_passwd__"]''').send_keys(newpassword)
    time.sleep(2)


@when(u'click the day')
def step_impl(context):
    dt = context.driver.find_element("id", "day")
    sel_dt = Select(dt)
    sel_dt.select_by_visible_text('13')
    time.sleep(2)


@when(u'click the month')
def step_impl(context):
    mon = context.driver.find_element("id", "month")
    sel_mon = Select(mon)
    sel_mon.select_by_visible_text('Mar')
    time.sleep(2)


@when(u'click the year')
def step_impl(context):
    yr = context.driver.find_element("id", "year")
    sel_yr = Select(yr)
    sel_yr.select_by_visible_text('1999')
    time.sleep(2)


@when(u'click on the gender female radio button')
def step_impl(context):
    context.driver.find_element("xpath","//label[@class='_58mt']/..//input[@class='_8esa'][1]").click()
    time.sleep(2)


@when(u'click on the Signup button')
def step_impl(context):
    context.driver.find_element("name", "websubmit").click()
    time.sleep(2)


@when(u'click on refresh')
def step_impl(context):
    context.driver.refresh()
    time.sleep(2)

@when(u'enter the username "{username}"')
def step_impl(context,username):
    pattern = r"\w+@gmail\.com"
    result = re.findall(pattern, username)
    assert result, "invalid conform_emailid"
    context.driver.find_element("xpath", "//input[@name='email']").send_keys(username)



@when(u'enter the password "{password}"')
def step_impl(context,password):
    context.driver.find_element("xpath", "//input[@name='pass' or @id='pass']").send_keys(password)


@when(u'click on login')
def step_impl(context):
    context.driver.find_element("xpath", "//button[@name='login']").click()
    time.sleep(2)

@then(u'close the browser')
def step_impl(context):
    context.driver.close()


