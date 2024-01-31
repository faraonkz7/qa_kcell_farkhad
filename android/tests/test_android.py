import pytest
import allure
from allure_commons.types import Severity

from android.page.calculator_page import CalculatorPage

@allure.title('Calc')
@allure.severity(Severity.BLOCKER)
class TestForm:

    # здесь только позитивные тест кейсы через параметризацию
    @pytest.mark.parametrize("a, operation, b, result", [(5, "+", 5, 10),
                                                         (5, "-", 5, 0),
                                                         (5, "/", 5, 1),
                                                         (5, "*", 5, 25),
                                                         (9999, "/", 11, 909)]
                             )
    def test_make_equity(self, mobile_driver, a, operation, b, result):
        driver = mobile_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('assertion'):
            assert calculator_page.is_result_equal(result)

