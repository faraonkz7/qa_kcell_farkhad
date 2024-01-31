import allure
import pytest
from api.api.Account import Account
from api.utilities import generate_random_username


@allure.feature("Позитивный тест на проверку авторизации пользователя")
@pytest.mark.positive
@pytest.mark.parametrize("username,password", [(generate_random_username(), "zx!!231Z")])
def test_authorized_user(username, password):
    user = Account(username, password)
    with allure.step("Запрос на добавление пользователя"):
        add_account_response = user.add_account()
    assert add_account_response.status_code == 201, "Неверный статус код в создании аккаунта"

    with allure.step("Запрос на авторизацию пользователя"):
        authorized_response = user.authorized()
    assert authorized_response.status_code == 200, "Неверный статус код в авторизации пользователя"
    assert bool(authorized_response.content) is True, "Неверный код ошибки"


@allure.feature("Негативный тест на проверку авторизации пользователя с данными, которых нет в системе")
@pytest.mark.negative
@pytest.mark.parametrize("username,password", [("user", "zxc!zxcqw!Z")])
def test_authorized_user_with_user_not_found(username, password):
    user = Account(username, password)
    with allure.step("Запрос на авторизацию пользователя"):
        response = user.authorized()
    assert response.status_code == 404, "Неверный статус код"
    assert response.json()["code"] == "1207", "Неверный код ошибки"
    assert response.json()["message"] == "User not found!"


@allure.feature("Негативный тест на проверку добавления пользователя с пустыми полями в запросе")
@pytest.mark.negative
@pytest.mark.parametrize("username,password", [("qweqwe", ""), ("", "zxc123z!")])
def test_authorized_user_with_empty_json_fields(username, password):
    user = Account(username, password)
    with allure.step("Запрос на авторизацию пользователя"):
        response = user.authorized()
    assert response.status_code == 400, "Неверный статус код"
    assert response.json()["code"] == "1200", "Неверный код ошибки"
    assert response.json()["message"] == "UserName and Password required.", "Неверное сообщение об ошибке"
