import datetime
import os
from time import sleep

import allure
import pytest
from selenium import webdriver
from form_page import FormPage


class TestDemo:

    @allure.feature("Позитивный тест на проверку добавления пользователя")
    @pytest.mark.positive
    def test_set_form(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='Фархад',
                last_name='Адилхан',
                user_email='adilkhan@farkhad.com',
                gender='Male',
                user_number='88005553535',
                date_of_birth='23.07.1996',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/cat.jpeg",
                current_address="г. Алматы, ул. Исаева, д. 30",
            )
        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, есть окно успеха
        assert page.is_success_message() == True

    @allure.feature("Не ввели имя, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_form_without_name(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='',
                last_name='Адилхан',
                user_email='adilkhan@farkhad.com',
                gender='Male',
                user_number='88005553535',
                date_of_birth='23.07.1996',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/cat.jpeg",
                current_address="г. Алматы, ул. Исаева, д. 30",
            )
        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False

    @allure.feature("Не выбрали гендер, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_without_gender(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='Фархад',
                last_name='Адилхан',
                user_email='adilkhan@farkhad.com',
                gender='',
                user_number='88005553535',
                date_of_birth='23.07.1996',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/cat.jpeg",
                current_address="г. Алматы, ул. Исаева, д. 30",
            )
        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False

    @allure.feature("Не нажали на submit, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_form_without_submit(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='Фархад',
                last_name='Адилхан',
                user_email='adilkhan@farkhad.com',
                gender='Male',
                user_number='88005553535',
                date_of_birth='23.07.1996',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/cat.jpeg",
                current_address="г. Алматы, ул. Исаева, д. 30",
            )

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False

    @allure.feature("Ввели не полный номер, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_form_without_full_number(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='Фархад',
                last_name='Адилхан',
                user_email='adilkhan@farkhad.com',
                gender='Male',
                user_number='8800555',
                date_of_birth='23.07.1996',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/cat.jpeg",
                current_address="г. Алматы, ул. Исаева, д. 30",
            )

        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False

    @allure.feature("Ввели неправильную почту, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_form_without_valid_email(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='Фархад',
                last_name='Адилхан',
                user_email='adilkhanfarkhad.com',
                gender='Male',
                user_number='8800555',
                date_of_birth='23.07.1996',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/cat.jpeg",
                current_address="г. Алматы, ул. Исаева, д. 30",
            )

        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    yield driver
    driver.quit()
