import allure


@allure.feature("feature测试")
class Testdemo:
    def setup_class(self):
        print("---setup_class---")

    def teardown_class(self):
        print("--teardown_class--")

    @allure.title("a的title")
    @allure.story("story测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")