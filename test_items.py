link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exist(browser):
    browser.get(link)
    buttons = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(buttons) == 1, "Add-to-basket button doesn't exist"