import allure
import pytest


@allure.feature("这是一级feature")
class Test_demo:
    def setup_class(self):
        print("---setup_class---")

    def teardown_class(self):
        print("--teardown_class--")

    @allure.title("test_a")
    @allure.story("这是二级story")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")