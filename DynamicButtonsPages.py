from BaseApp import BaseApp

class DynamicButtonsLocator:
    BUTTON_0 = "#button00"
    BUTTON_1 = "#button01"
    BUTTON_2 = "#button02"
    BUTTON_3 = "#button03"
    CONFIRM_TEXT = "text=All Buttons Clicked"

class SearchHelper(BaseApp):
    def __init__(self, page):
        super().__init__(page, "https://testpages.eviltester.com/styled/dynamic-buttons-simple.html")
        self.go_to_site()

    def click_button_0(self):
        self.page.click(DynamicButtonsLocator.BUTTON_0)

    def click_button_1(self):
        self.page.click(DynamicButtonsLocator.BUTTON_1)

    def click_button_2(self):
        self.page.click(DynamicButtonsLocator.BUTTON_2)

    def click_button_3(self):
        self.page.click(DynamicButtonsLocator.BUTTON_3)

    def check_text(self):
        return self.page.is_visible(DynamicButtonsLocator.CONFIRM_TEXT)
