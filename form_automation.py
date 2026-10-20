from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import csv
browser = webdriver.Chrome()
target_url = "https://www.qapractice.com/practice-forms"
browser_wait = WebDriverWait(browser, 10)
PASS_MARK = 50
submitted = 0
skipped = 0

def fill_in_info(field_id, value):
    browser.find_element(By.ID, field_id).send_keys(value)

def choose(field_id, text):
    Select(browser.find_element(By.ID, field_id)).select_by_visible_text(text)

def  click_on_element(element_id):
    element = browser.find_element(By.ID, element_id)
    ActionChains(browser).scroll_to_element(element).perform()
    element.click()

def go_back_to_form():
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn"))).click()
    
try:
    with open("Site.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)

        for row in reader:
            if not row or not any(row):
                continue
            country, title, first, last, dob, doj, email, phone, method, grade = [cell.strip() for cell in row[:10]] #reading rows
            grade = row[10].strip() #due to weird glitches happening when submitting it says invalid grade
            try:
                score = float(grade.split("/")[0])
            except ValueError:
                print(f"Skipped: {first} {last} (invalid grade: '{grade}')")
                skipped += 1
                continue

            if score < PASS_MARK:
                print(f"Skipped: {first} {last} (failed, {score:g}/70)")
                skipped += 1
                continue

            browser.get(target_url)
            browser_wait.until(EC.visibility_of_element_located((By.ID, "forms-country")))

            choose("forms-country", country)
            choose("forms-title", title)
            fill_in_info("forms-first-name", first)
            fill_in_info("forms-last-name", last)
            fill_in_info("forms-dob", dob)
            fill_in_info("forms-doj", doj)
            fill_in_info("forms-email", email)
            fill_in_info("forms-phone-number", phone)
            click_on_element(f"forms-comm-{method.lower()}")
            click_on_element("forms-submit")
            go_back_to_form()
            print(f"Submitted: {first} {last} ({score:g}/70)")
            submitted += 1
    print(f"Done. Submitted: {submitted}, Skipped: {skipped}")
finally:
    browser.quit()
