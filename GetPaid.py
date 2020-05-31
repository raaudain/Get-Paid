from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import autoit

# Between the quotes, enter your credentials. Make sure there are no extra spaces.
username = ""
password = ""

# Between the quotes, enter the time you come in and the time you leave. Don't forget AM and PM.
timeIn = "9:00 AM"
timeOut = "6:00 PM"

# Lunch break
lunch = "1:00"

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.get("https://my.springahead.com/go/Account/Logon/REPLACE_WITH_COMPANY'S_NAME/")

userID = browser.find_elements_by_id("UserName")

userID[0].send_keys(username)
browser.find_element_by_id("Password").send_keys(password)
browser.find_element_by_class_name("submit").click()

browser.find_element_by_class_name("small").click()

workday = 3

while workday <= 11:

    try:
        browser.find_element_by_css_selector("tbody.timedaySectionBody:nth-child("+str(workday)+") > tr:nth-child(2) > td:nth-child(2) > "
                                             "div:nth-child(1) > button:nth-child(1)").click()
        select = Select(browser.find_element_by_css_selector("#timedayTable > tbody:nth-child("+str(workday)+") > "
                                                             "tr.timeRowModel.editor_content.timedayEdit.timedayCalc > "
                                                             "td.timedayProject > select"))
        select.select_by_index(1)
        browser.find_element_by_class_name("timein_input").send_keys(timeIn)
        browser.find_element_by_class_name("timeout_input").send_keys(timeOut)
        browser.find_element_by_class_name("timebreak_input").send_keys(lunch)
        browser.find_element_by_css_selector("tr.timedayEdit:nth-child(5) > td:nth-child(5) > button:nth-child(1)").click()
    except:
        pass

    time.sleep(0.5)

    workday += 2

# Clicks submit button
browser.find_element_by_id("submitall").click()

time.sleep(1)

# Does the final submission for the timecard
autoit.send("{ENTER}")

time.sleep(10)

browser.quit()