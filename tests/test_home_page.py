import pytest

from pages.home_Page import HomePageQA
from tests.conftest import browser_instance


class TestHomePage:
    @pytest.fixture(autouse=True)
    def pre_run(self, browser_instance):
        self.home_page = HomePageQA(browser_instance)

    def test_home_page(self):
        self.home_page.text_box()
        self.home_page.check_box()
        self.home_page.radio_btn()


