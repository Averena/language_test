link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language(browser):
    browser.get(link)
    ell = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert ell, "Is OK"