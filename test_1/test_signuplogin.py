import datetime
import time

import pytest
from POM.signup_login import Facebook
from DATA.reading_objects import ReadExcel
from LIBRARY.config import Config


class TestSignupLoginPage:
    read_xl = ReadExcel()
    details = read_xl.read_test_data(Config.read_test_data)

    @pytest.mark.parametrize("firstname_value,surname_value,email_id,conemail_id,newpassword_value,username_value,password_value", details)
    def test_Signuplogin(self, firstname_value, surname_value, email_id, conemail_id, newpassword_value, username_value,password_value, _driver):
        lp = Facebook(_driver)
        lp.Createnewaccount()
        lp.firstname(firstname_value)
        lp.surname(surname_value)
        lp.emailid(email_id)
        lp.con_emailid(conemail_id)
        # time.sleep(2)
        lp.new_password(newpassword_value)
        # time.sleep(2)
        lp.date()
        # time.sleep(2)
        lp.month()
        # time.sleep(2)
        lp.year()
        # time.sleep(2)
        lp.gender()
        # time.sleep(2)
        lp.signup()
        # time.sleep(2)
        lp.username(username_value)
        # time.sleep(2)
        lp.password(password_value)
        # time.sleep(2)
        lp.login()
        time.sleep(5)
        # lp.close()
