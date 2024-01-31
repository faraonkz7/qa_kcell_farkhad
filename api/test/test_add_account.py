import allure
import pytest
from api.api.Account import Account
from api.utilities import generate_random_username


@allure.feature("Позитивный тест на проверку добавления пользователя")
@pytest.mark.positive
@pytest.mark.parametrize("username,password", [(generate_random_username(), "zx!!231Z")])
def test_add_account(username, password):
    user = Account(username, password)
    with allure.step("Запрос на добавление пользователя"):
        response = user.add_account()
    assert response.status_code == 201, "Неверный статус код"
    assert response.json()["userId"], "Пустой userId"
    assert response.json()["username"] == username, "Неверный username"
    assert response.json()["books"] == [], "Неверное значение books"


@allure.feature("Негативный тест на проверку добавления пользователя с не валидным паролем")
@pytest.mark.negative
@pytest.mark.parametrize("username,password", [("user", "zxzxczxz"), ("user", "12345678"), ("user", "zxcx1231"),
                                                ("user", "!!!!...."), ("user", "zxcz12!!"), ("user", "1231!!!!"),
                                                ("user", "zxcxc!!!"), ("user", "ZZZZZZZZ"), ("user", "zczzxcZ!"),
                                                ("user", "zxcxcZZZ"), ("user", "ZZZZZ!!!"), ("user", "ZZZZZ123"),
                                                ("user", "zxcz123Z"), ("user", "1231Z3!!"), ("user", "z!Z1")])
def test_add_account_with_negative_password(username, password):
    user = Account(username, password)
    with allure.step("Запрос на добавление пользователя"):
        response = user.add_account()
    assert response.status_code == 400, "Неверный статус код"
    assert response.json()["code"] == "1300", "Неверный код ошибки"
    assert response.json()["message"] == ("Passwords must have at least one non alphanumeric character, "
                                          "one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), "
                                          "one special character and Password must be eight characters "
                                          "or longer."), "Неверное сообщение об ошибке"


@allure.feature("Негативный тест на проверку добавления пользователя с данными уже существующего пользователя")
@pytest.mark.negative
@pytest.mark.parametrize("username,password", [("qweqwe", "12Zzxc!!")])
def test_add_account_with_user_exists(username, password):
    user = Account(username, password)
    with allure.step("Запрос на добавление пользователя"):
        response = user.add_account()
    assert response.status_code == 406, "Неверный статус код"
    assert response.json()["code"] == "1204", "Неверный код ошибки"
    assert response.json()["message"] == "User exists!", "Неверное сообщение об ошибке"


@allure.feature("Негативный тест на проверку добавления пользователя с пустыми полями в запросе")
@pytest.mark.negative
@pytest.mark.parametrize("username,password", [("qweqwe", ""), ("", "zxc123z!")])
def test_add_account_with_empty_json_fields(username, password):
    user = Account(username, password)
    with allure.step("Запрос на добавление пользователя"):
        response = user.add_account()
    assert response.status_code == 400, "Неверный статус код"
    assert response.json()["code"] == "1200", "Неверный код ошибки"
    assert response.json()["message"] == "UserName and Password required.", "Неверное сообщение об ошибке"