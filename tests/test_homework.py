from selene import browser, have, be
import pytest
import os


def test_form_demoqa(browser_managment):
    #removing excess
    browser.element("footer").execute_script('element.remove()')
    #test body
    browser.should(have.title("DEMOQA"))
    browser.element("#firstName").should(be.blank).type("тест")
    browser.element("#lastName").should(be.blank).type("тестов")
    browser.element("#userEmail").should(be.blank).type("test@mail.ru")
    browser.element("[for=gender-radio-1]").click()
    browser.element("#userNumber").should(be.blank).type("88888888888")
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__month-select>option[value="1"]').click()
    browser.element('.react-datepicker__year-select>option[value="1999"]').click()
    browser.element('[aria-label="Choose Thursday, February 18th, 1999"]').click()
    browser.element("#subjectsInput").should(be.blank).type("Engl").press_enter()
    browser.element("[for=hobbies-checkbox-1]").click()
    browser.element('[id="uploadPicture"]').send_keys(os.getcwd() + '/test.jpg')
    browser.element("#currentAddress").should(be.blank).type("Testovaya street 35")
    browser.element("#react-select-3-input").should(be.blank).type("Utt").press_enter()
    browser.element("#react-select-4-input").should(be.blank).type("Ag").press_enter()
    browser.element('[id="submit"]').submit()


    #checks
    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    browser.element("//tbody/tr[1]/td[2]").should(have.text("тест тестов"))
    browser.element("//tbody/tr[2]/td[2]").should(have.text("test@mail.ru"))
    browser.element("//tbody/tr[3]/td[2]").should(have.text("Male"))
    browser.element("//tbody/tr[4]/td[2]").should(have.text("8888888888"))
    browser.element("//tbody/tr[5]/td[2]").should(have.text("18 February,1999"))
    browser.element("//tbody/tr[6]/td[2]").should(have.text("English"))
    browser.element("//tbody/tr[7]/td[2]").should(have.text("Sports"))
    browser.element("//tbody/tr[8]/td[2]").should(have.text("test.jpg"))
    browser.element("//tbody/tr[9]/td[2]").should(have.text("Testovaya street 35"))
    browser.element("//tbody/tr[10]/td[2]").should(have.text("Uttar Pradesh Agra"))


