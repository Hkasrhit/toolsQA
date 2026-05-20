import logging
import time

from playwright.sync_api import Page, expect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HomePageQA:
    def __init__(self, instance: Page):
        self.driver = instance

    def text_box(self):
        print(f'{self.driver.title()}')
        self.driver.locator('a[href="/elements"]').click()
        self.driver.locator('a[href="/text-box"]').click()
        self.driver.get_by_placeholder('Full Name', exact=True).fill('harshit Kushwah')
        self.driver.get_by_placeholder('name@example.com', exact=True).fill('harshit.k@gmail.com')
        self.driver.get_by_placeholder('Current Address', exact=True).fill('gwalior')
        self.driver.locator('textarea[id="permanentAddress"]').fill("hazira")
        self.driver.get_by_text('Submit').click()
        expect(self.driver.locator('div[id="output"]')).to_be_visible()

    def check_box(self):
        self.driver.locator('a[href="/checkbox"]').click()
        expect(self.driver.get_by_role('treeitem')).to_be_visible()
        self.driver.get_by_role('checkbox').check()
        expect(self.driver.locator('div[id="result"]'))


    def radio_btn(self):
        self.driver.locator('a[href="/radio-button"]').click()
        all_options = self.driver.locator('div.col-auto.form-check').all()
        for options in all_options:
            if options.text_content() == "Yes":
                options.click()
            else:
                logger.info("given option is not available")
            time.sleep(20)