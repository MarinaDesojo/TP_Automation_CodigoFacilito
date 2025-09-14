import pytest
#page objects
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from pages.home_page import HomePage
from pages.header_page import HeaderPage
from conftest import driver
from utils.config import EMAIL_USER, PASSWORD, FIRST_NAME, LAST_NAME, ZIP_CODE
from utils.config import PASSWORD_MAX_CHAR, PASSWORD_MAX_CHAR_PLUS1, EMAIL_MAX_CHAR, EMAIL_MAX_CHAR_PLUS1, EMAIL_NO_AT, EMAIL_NO_TEXT_POST_AT, EMAIL_NO_TEXT_PRE_AT, EMAIL_ONLY_AT, EMAIL_DOUBLE_AT, EMAIL_SPECIAL_CH_1, EMAIL_SPECIAL_CH_2, EMAIL_SPECIAL_CH_3, EMAIL_SPECIAL_CH_4, EMAIL_SPECIAL_CH_5, EMAIL_SPECIAL_CH_6, EMAIL_SPECIAL_CH_7

@pytest.mark.login
@pytest.mark.happypath
def test_login_success(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_success(EMAIL_USER, PASSWORD)
    login.verify_logged_in_text()
# Usually on the login page I would test registered emails and passwords, but on this website that is not the case, so the approach is a little different
# Usually there would be no need to test valid emails on the login page, only on the sign up page, because the user would not have been able to register it on the first place

@pytest.mark.login
@pytest.mark.happypath
def test_login_success_max_email_char(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_success(EMAIL_MAX_CHAR, PASSWORD)
    login.verify_logged_in_text()

@pytest.mark.login
@pytest.mark.happypath
def test_login_success_max_password_char(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_success(EMAIL_USER, PASSWORD_MAX_CHAR)
    login.verify_logged_in_text()

@pytest.mark.e2e
@pytest.mark.login
@pytest.mark.happypath
def test_login_success_e2e(driver):
    homepage = HomePage(driver)
    header = HeaderPage(driver)
    login = LoginPage(driver)

    homepage.load()
    header.go_to_login_page()
    login.fill_login_form_success(EMAIL_USER, PASSWORD)
    login.verify_logged_in_text()
    login.go_to_home()

@pytest.mark.login
@pytest.mark.fail
def test_login_empty_fields_fail(driver):
    login = LoginPage(driver)

    login.load()
    login.empty_login_form()

@pytest.mark.login
@pytest.mark.fail
def test_login_space_fields_fail(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(" ", " ")

@pytest.mark.login
@pytest.mark.fail
def test_login_no_email(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail("", PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_no_password(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_USER, "")

@pytest.mark.login
@pytest.mark.fail
def test_login_max_char_email_plus1(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_MAX_CHAR_PLUS1, " ")
# Fail, unknown character limit on input, fail detected

@pytest.mark.login
@pytest.mark.fail
def test_login_max_char_password_plus1(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_USER, PASSWORD_MAX_CHAR_PLUS1)
# Fail, unknown character limit on input, fail detected

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_1(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_NO_AT, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_2(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_NO_TEXT_POST_AT, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_3(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_NO_TEXT_PRE_AT, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_4(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_ONLY_AT, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_5(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_DOUBLE_AT, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_6(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_SPECIAL_CH_1, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_7(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_SPECIAL_CH_2, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_8(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_SPECIAL_CH_3, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_9(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_SPECIAL_CH_4, PASSWORD)

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_10(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_SPECIAL_CH_5, PASSWORD)
# Fails, bug detected

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_11(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_SPECIAL_CH_6, PASSWORD)
# Fails, bug detected

@pytest.mark.login
@pytest.mark.fail
def test_login_wrong_email_12(driver):
    login = LoginPage(driver)

    login.load()
    login.fill_login_form_fail(EMAIL_SPECIAL_CH_7, PASSWORD)
# Fails, bug detected


@pytest.mark.sign_up
@pytest.mark.happypath
def test_sign_up_success(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_success(FIRST_NAME, LAST_NAME, EMAIL_USER, ZIP_CODE, PASSWORD)
    signup.verify_signed_up_text()
    signup.go_to_home()

@pytest.mark.sign_up
@pytest.mark.happypath
def test_sign_up_email_and_space_fields_success(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_success(" ", " ", EMAIL_USER, " ", " ")
# Email input field is the only one with conditions to meet, set by the browser, same as login
# There are no restrictions or conditions to meet on the other fields

@pytest.mark.e2e
@pytest.mark.sign_up
@pytest.mark.happypath
def test_sign_up_success_e2e(driver):
    homepage = HomePage(driver)
    header = HeaderPage(driver)
    signup = SignUpPage(driver)

    homepage.load()
    header.go_to_signup_page()
    signup.fill_sign_up_form_success(FIRST_NAME, LAST_NAME, EMAIL_USER, ZIP_CODE, PASSWORD)
    signup.verify_signed_up_text()
    signup.go_to_home()

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_empty_fields_fail(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.empty_sign_up_form()

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_space_fields_fail(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", " ", " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_1(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_NO_AT, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_2(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_NO_TEXT_POST_AT, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_3(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_NO_TEXT_PRE_AT, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_4(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_ONLY_AT, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_5(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_DOUBLE_AT, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_6(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_SPECIAL_CH_1, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_7(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_SPECIAL_CH_2, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_8(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_SPECIAL_CH_3, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_9(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_SPECIAL_CH_4, " ", " ")

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_10(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_SPECIAL_CH_5, " ", " ")
# Fails, bug detected

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_11(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_SPECIAL_CH_6, " ", " ")
# Fails, bug detected

@pytest.mark.sign_up
@pytest.mark.fail
def test_sign_up_wrong_email_and_space_fields_fail_12(driver):
    signup = SignUpPage(driver)

    signup.load()
    signup.fill_sign_up_form_fail(" ", " ", EMAIL_SPECIAL_CH_7, " ", " ")
# Fails, bug detected


