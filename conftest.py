from selene import browser
import pytest


@pytest.fixture
def browser_managment():
    browser.config.hold_browser_open = True
    browser.open("https://demoqa.com/automation-practice-form")
