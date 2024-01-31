import requests
from requests import Response
from ..settings import ACCOUNT_USER_URL, ACCOUNT_GENERATE_TOKEN_URL, ACCOUNT_AUTHORIZED


class Account:

    def __init__(self, username: str, password: str):
        self.user_id = None
        self.username = username
        self.password = password

    def add_account(self) -> Response:
        response = requests.post(
            url=ACCOUNT_USER_URL,
            json={"userName": self.username, "password": self.password}
        )
        self.user_id = response.json()["userID"]
        return response

    def generate_token(self) -> Response:
        response = requests.post(
            url=ACCOUNT_GENERATE_TOKEN_URL,
            json={"userName": self.username, "password": self.password}
        )
        return response

    def authorized(self) -> Response:
        response = requests.post(
            url=ACCOUNT_AUTHORIZED,
            json={"userName": self.username, "password": self.password}
        )
        return response

    def delete_account(self) -> Response:
        response = requests.delete(url=ACCOUNT_USER_URL + f'/{self.user_id}')
        return response

    def get_account(self) -> Response:
        response = requests.get(url=ACCOUNT_USER_URL + f'/{self.user_id}')
        return response
