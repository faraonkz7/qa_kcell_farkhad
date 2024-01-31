from selenium.webdriver.common.by import By

zero_xpath = (By.ID, "com.miui.calculator:id/btn_0_s")
one_xpath = (By.ID, "com.miui.calculator:id/btn_1_s")
two_xpath = (By.ID, "com.miui.calculator:id/btn_2_s")
three_xpath = (By.ID, "com.miui.calculator:id/btn_3_s")
four_xpath = (By.ID, "com.miui.calculator:id/btn_4_s")
five_xpath = (By.ID, "com.miui.calculator:id/btn_5_s")
six_xpath = (By.ID, "com.miui.calculator:id/btn_6_s")
seven_xpath = (By.ID, "com.miui.calculator:id/btn_7_s")
eight_xpath = (By.ID, "com.miui.calculator:id/btn_8_s")
nine_xpath = (By.ID, "com.miui.calculator:id/btn_9_s")
plus_xpath = (By.ID, "com.miui.calculator:id/btn_plus_s")
minus_xpath = (By.ID, "com.miui.calculator:id/btn_minus_s")
mul_xpath = (By.ID, "com.miui.calculator:id/btn_mul_s")
divide_xpath = (By.ID, "com.miui.calculator:id/btn_div_s")
percent_xpath = (By.ID, "com.miui.calculator:id/btn_percent_s")
equal_xpath = (By.ID, "com.miui.calculator:id/btn_equal_s")
expression_xpath = (By.ID, "com.miui.calculator:id/expression")
result_xpath = (By.ID, "com.miui.calculator:id/result")
clear_xpath = (By.ID, "com.miui.calculator:id/btn_c_s")

class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def select_buton(self, option):
        if option == 0:
            self.driver.find_element(*zero_xpath).click()
        if option == 1:
            self.driver.find_element(*one_xpath).click()
        if option == 2:
            self.driver.find_element(*two_xpath).click()
        if option == 3:
            self.driver.find_element(*three_xpath).click()
        if option == 4:
            self.driver.find_element(*four_xpath).click()
        if option == 5:
            self.driver.find_element(*five_xpath).click()
        if option == 6:
            self.driver.find_element(*six_xpath).click()
        if option == 7:
            self.driver.find_element(*seven_xpath).click()
        if option == 8:
            self.driver.find_element(*eight_xpath).click()
        if option == 9:
            self.driver.find_element(*nine_xpath).click()
        if option == "+":
            self.driver.find_element(*plus_xpath).click()
        if option == "-":
            self.driver.find_element(*minus_xpath).click()
        if option == "/":
            self.driver.find_element(*divide_xpath).click()
        if option == "*":
            self.driver.find_element(*mul_xpath).click()
        if option == "%":
            self.driver.find_element(*percent_xpath).click()
        if option == "=":
            self.driver.find_element(*equal_xpath).click()
        if option == "c":
            self.driver.find_element(*clear_xpath).click()

    def click_to(self, option):
        if str(option).isdigit() and option >9:
            for op in option.__str__():
                self.select_buton(int(op))
        else:
            self.select_buton(option)


    def operate(self, a, operation, b):
        self.click_to("c")
        self.click_to(a)
        self.click_to(operation)
        self.click_to(b)
        self.click_to("=")

    def is_result_equal(self, result):
        res = self.driver.find_element(*result_xpath).text
        print("result is = "+res)
        return str(result) in res

    def open_app(self):
        self.driver.activate_app('com.miui.calculator')
