import allure
import pytest
from api.api.Account import Account
from api.utilities import generate_random_username


@allure.feature("Позитивный тест на проверку удаления пользователя")
@pytest.mark.xfail
@pytest.mark.parametrize("username,password", [(generate_random_username(), "zx!!231Z")])
def test_delet_user(username, password):
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

    with allure.step("Запрос на удаление пользователя"):
        delete_account_response = user.delete_account()
    assert delete_account_response.status_code == 200
    assert delete_account_response.json()["code"], "Неверный код удаления аккаунта"
    assert delete_account_response.json()["message"] == "", "Неверное сообщение об результате"
