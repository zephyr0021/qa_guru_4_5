from selene import browser


def test_add_todos():
    browser.config.hold_browser_open = True
    browser.open("https://ya.ru/")

