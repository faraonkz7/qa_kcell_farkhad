import allure
import pytest
from api.api.Account import Account
from api.utilities import generate_random_username


@allure.feature("Позитивный тест на проверку получения информации о пользователе")
@pytest.mark.xfail
@pytest.mark.parametrize("username,password", [(generate_random_username(), "zx!!231Z")])
def test_get_user_info(username, password):
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

    with allure.step("Запрос на получение информации о пользователе"):
        get_user_response = user.get_account()
    assert get_user_response.status_code == 200
    assert get_user_response.json()["userId"], "Пустой userId"
    assert get_user_response.json()["username"] == username, "Неверный username"
    assert get_user_response.json()["books"] == [], "Неверное значение books"
