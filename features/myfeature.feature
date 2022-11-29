Feature: Signup/login
  Scenario Outline: User should be able to Signup and login into the application
    Given Open the chrome browser enter the valid URL
    When click on createnewaccount button
    And enter the first name "<firstname>"
    And enter the last name "<lastname>"
    And enter the email_id "<email_id>"
    And re_enter the confirm_emailid "<confirm_emailid>"
    And enter the new password "<newpassword>"
    And click the day
    And click the month
    And click the year
    And click on the gender female radio button
    And click on the Signup button
    And click on refresh
    And enter the username "<username>"
    And enter the password "<password>"
    And click on login
    Then close the browser
    Examples:
      |firstname|lastname|email_id |confirm_emailid |newpassword|username|password|
      |Ruby |Natalie|rubynatalie976@gmail.com|rubynatalie976@gmail.com|Rubynatalie32|rubynatalie976@gmail.com|Rubynatalie32|
      |Jessie |Hirst |jessiehirst01@gmail.com|jessiehirst01@gmail.com|Jessiehirst13 |jessiehirst01@gmail.com|Jessiehirst13 |
      |Parigny|gowda|parignya1999@gmail.com|parignya1999@gmail.com |Sumithra@1999   |kmaadhya2727@gmail.com |Sumithra@1999 |
      |Anya|Paiz|paizanya13@gmail.com|paizanya13@gmail.com|AnyaPaiz@12|paizanya13@gmail.com |AnyaPaiz@12 |
      |Aadhya|Reddy |aadhyareddy13@gmail.com|aadhyareddy13@gmail.com||aadhyareddy13@gmail.com|45679|
