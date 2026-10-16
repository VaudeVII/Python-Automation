from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import csv

browser = webdriver.Chrome()
target_url = "https://www.qapractice.com/practice-forms"
wait = WebDriverWait(browser, 10)

def country_input(country):
    country_browser = browser.find_element(By.ID, "forms-country")
    Select(country_browser).select_by_visible_text(country)

def title_input(title):
    title_browser = browser.find_element(By.ID, "forms-title")
    Select(title_browser).select_by_visible_text(title)

def first_name(name):
    first_name_browser = browser.find_element(By.ID, "forms-first-name")
    first_name_browser.send_keys(name)

def last_name(name):
    last_name_browser = browser.find_element(By.ID, "forms-last-name")
    last_name_browser.send_keys(name)

def date_of_birth_input(dob):
    dob_browser = browser.find_element(By.ID, "forms-dob")
    dob_browser.send_keys(dob)

def date_of_joining_input(doj):
    doj_browser = browser.find_element(By.ID, "forms-doj")
    doj_browser.send_keys(doj)

def email_input(email):
    email_browser = browser.find_element(By.ID, "forms-email")
    email_browser.send_keys(email)

def phone_input(phone):
    phone_browser = browser.find_element(By.ID, "forms-phone-number")
    phone_browser.send_keys(phone)

def communication_input(method):
    communication = browser.find_element(By.ID, f"forms-comm-{method.lower()}")
    ActionChains(browser).scroll_to_element(communication).perform()
    communication.click()

def submit_form():
    submit_browser = browser.find_element(By.ID, "forms-submit")
    ActionChains(browser).scroll_to_element(submit_browser).perform()
    submit_browser.click()

def go_back_to_form(): #<button type="button" class="mt-3 btn btn-primary">Go Back to Form</button>
    go_back_to_form_browser = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
    go_back_to_form_browser.click()

with open("Site.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)

    for row in reader:
        if not row or not any(row):
            continue

        country = row[0].strip()
        title = row[1].strip()
        first = row[2].strip()
        last = row[3].strip()
        dob = row[4].strip()
        doj = row[5].strip()
        email = row[6].strip()
        phone = row[7].strip()
        method = row[8].strip()

        browser.get(target_url)

        wait.until(
            EC.visibility_of_element_located((By.ID, "forms-country"))
        )

        country_input(country)
        title_input(title)
        first_name(first)
        last_name(last)
        date_of_birth_input(dob)
        date_of_joining_input(doj)
        email_input(email)
        phone_input(phone)
        communication_input(method)
        submit_form()
        go_back_to_form()
        print("Submitted:", first, last)
browser.quit()
