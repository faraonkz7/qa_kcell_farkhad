import allure
import pytest
from api.api.Account import Account
from api.utilities import generate_random_username


@allure.feature("Позитивный тест на проверку формирования токена пользователя")
@pytest.mark.positive
@pytest.mark.parametrize("username,password", [(generate_random_username(), "zx!!231Z")])
def test_generate_token(username, password):
    user = Account(username, password)
    with allure.step("Запрос на добавление пользователя"):
        add_account_response = user.add_account()
    assert add_account_response.status_code == 201, "Неверный статус код в создании аккаунта"

    with allure.step("Запрос на авторизацию пользователя"):
        authorized_response = user.authorized()
    assert authorized_response.status_code == 200, "Неверный статус код в авторизации пользователя"
    assert bool(authorized_response.content) is True, "Неверный код ошибки"

    with allure.step("Запрос на формирование токена пользователя"):
        generate_token_response = user.generate_token()
    assert generate_token_response.status_code == 200, "Неверный статус код"
    assert generate_token_response.json()["token"], "Неверный код ошибки"
    assert generate_token_response.json()["expires"], "Неверное время жизни токена"
    assert generate_token_response.json()["status"] == "Success", "Неверный статус"
    assert generate_token_response.json()["result"] == "User authorized successfully.", "Неверное сообщение о результате"


@allure.feature("Негативный тест на проверку формирования токена пользователя")
@pytest.mark.negative
@pytest.mark.parametrize("username,password", [("user", "zxc!Z1231")])
def test_generate_token_for_none_authorized_user(username, password):
    user = Account(username, password)
    with allure.step("Запрос на формирование токена пользователя"):
        response = user.generate_token()
    assert response.status_code == 200, "Неверный статус код"
    assert response.json()["token"] is None, "Неверный код ошибки"
    assert response.json()["expires"] is None, "Неверное время жизни токена"
    assert response.json()["status"] == "Failed", "Неверный статус"
    assert response.json()["result"] == "User authorization failed.", "Неверное сообщение о результате"


@allure.feature("Негативный тест на проверку формирования токена пользователя с пустыми полями в запросе")
@pytest.mark.negative
@pytest.mark.parametrize("username,password", [("qweqwe", ""), ("", "zxc123z!")])
def test_generate_token_with_empty_json_fields(username, password):
    user = Account(username, password)

    with allure.step("Запрос на формирование токена пользователя"):
        response = user.generate_token()
    assert response.status_code == 400, "Неверный статус код"
    assert response.json()["code"] == "1200", "Неверный код ошибки"
    assert response.json()["message"] == "UserName and Password required.", "Неверное сообщение об ошибке"
