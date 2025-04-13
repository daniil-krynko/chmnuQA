import pytest
from DynamicButtonsPages import SearchHelper

def test_dynamic_buttons(browser):
    page = SearchHelper(browser)  
    
    page.click_button_0()
    page.click_button_1()
    page.click_button_2()
    page.click_button_3()
    
    assert page.check_text()
