from selene import browser, have, be
import pytest


def test_form_demoqa(browser_managment):
    browser.should(have.title("DEMOQA"))
    browser.element("#firstName").should(be.blank).type("тест")
    browser.element("#lastName").should(be.blank).type("тестов")
    browser.element("#userEmail").should(be.blank).type("test@mail.ru")
    browser.element("[for=gender-radio-1]").click()
    browser.element("#userNumber").should(be.blank).type("88888888888")



