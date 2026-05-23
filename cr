[1mdiff --git a/pages/__pycache__/home_Page.cpython-312.pyc b/pages/__pycache__/home_Page.cpython-312.pyc[m
[1mindex 68bb3b3..a4a7f10 100644[m
Binary files a/pages/__pycache__/home_Page.cpython-312.pyc and b/pages/__pycache__/home_Page.cpython-312.pyc differ
[1mdiff --git a/pages/home_Page.py b/pages/home_Page.py[m
[1mindex 4dffcd3..d938138 100644[m
[1m--- a/pages/home_Page.py[m
[1m+++ b/pages/home_Page.py[m
[36m@@ -35,6 +35,10 @@[m [mclass HomePageQA:[m
         for options in all_options:[m
             if options.text_content() == "Yes":[m
                 options.click()[m
[32m+[m[32m                expect(self.driver.locator('p.mt-3')).to_contain_text("You have selected",ignore_case=True)[m
             else:[m
                 logger.info("given option is not available")[m
[31m-            time.sleep(20)[m
\ No newline at end of file[m
[32m+[m
[32m+[m[32m    def web_tables(self):[m
[32m+[m[32m        self.driver.locator('a[href="/webtables"]').click()[m
[32m+[m[32m        expect(self.driver.locator('h1.text-center')).to_contain_text('web tables',ignore_case=True)[m
\ No newline at end of file[m
