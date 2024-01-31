from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

first_name = (By.CSS_SELECTOR, "#firstName")
last_name = (By.CSS_SELECTOR, "#lastName")
user_email = (By.ID, "userEmail")
gender_css = (By.CSS_SELECTOR, '#genterWrapper > div .custom-control-label')
user_number = (By.ID, "userNumber")
date_of_birth_input = (By.ID, "dateOfBirthInput")
subjects_input = (By.XPATH, '//*[@id="subjectsInput"]')
hobies = (By.CSS_SELECTOR, '#hobbiesWrapper > div .custom-control-label')
picture = (By.ID, "uploadPicture")
current_address = (By.ID, "currentAddress")
submit_btn = (By.ID, "submit")


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.CSS_SELECTOR, "#firstName")
        self.last_name = (By.CSS_SELECTOR, "#lastName")
        self.user_email = (By.ID, "userEmail")
        self.gender_css = (By.CSS_SELECTOR, '#genterWrapper > div .custom-control-label')
        self.user_number = (By.ID, "userNumber")
        self.date_of_birth_input = (By.ID, "dateOfBirthInput")
        self.subjects_input = (By.XPATH, '//*[@id="subjectsInput"]')
        self.hobies = (By.CSS_SELECTOR, '#hobbiesWrapper > div .custom-control-label')
        self.picture = (By.ID, "uploadPicture")
        self.current_address = (By.ID, "currentAddress")

    def move_to_element(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def set_gender(self, gender='Male'):
        elements = self.driver.find_elements(*gender_css)
        for elem in elements:
            if elem.text == gender:
                self.move_to_element(elem)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(elem)).click()

    def set_date(self, date_of_birth):
        pick_date = self.driver.find_element(*date_of_birth_input)
        pick_date.send_keys(Keys.CONTROL + "a")
        pick_date.send_keys(
            datetime.datetime.strftime(datetime.datetime.strptime(date_of_birth, '%d.%m.%Y'), '%d %b %Y'))
        pick_date.send_keys(Keys.ENTER)

    def set_subjects(self, subjects):
        subject = self.driver.find_element(*subjects_input)
        for sub in subjects:
            subject.send_keys(sub)
            subject.send_keys(Keys.ENTER)

    def set_hobbies(self, hobbies):
        elements = self.driver.find_elements(*hobies)
        for elem in elements:
            if elem.text in hobbies:
                self.move_to_element(elem)
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(elem)).click()

    def upload_picture(self, picture_path):
        self.driver.find_element(*picture).send_keys(picture_path)

    def set_address(self, address):
        self.driver.find_element(*current_address).send_keys(address)

    def submit(self):
        self.driver.find_element(*submit_btn).click()

    def fill_form(self,
                  first_name,
                  last_name,
                  user_email,
                  gender,
                  user_number,
                  date_of_birth,
                  subjects,
                  hobies,
                  picture,
                  current_address
                  ):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.user_email).send_keys(user_email)

        self.set_gender(gender)

        self.driver.find_element(*self.user_number).send_keys(user_number)

        self.set_date(date_of_birth)
        self.set_subjects(subjects)
        self.set_hobbies(hobies)
        self.upload_picture(picture)

        self.driver.find_element(*self.current_address).send_keys(current_address)

    def is_success_message(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".modal-footer")
            return True
        except NoSuchElementException:
            return False
