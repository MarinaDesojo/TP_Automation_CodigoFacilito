# TP_Automation_CodigoFacilito

## Information
### This project implements automated testing using:
- 🐍 Python
- 🧪 Pytest
- 🕸️ Selenium WebDriver for browser interaction
- 🧱 Page Object Model (POM) to keep code DRY

Tests are designed to validate key flows on both web and API.

### Project architecture:

    📁 UI_project/           
        📁 tests/          → Directories organized by endpoint, each with its own test.py and conftest.py  
        📁 reports/        → Report directory for test generated reports  
        📁 utils/          → Helpers like api helper, fixture, settings and config  
    📁 API_project/        
        📁 tests/          → Test.py files organized   
        📁 pages/          → POM classes for each URL   
        📁 utils/          → Helpers like driver factory, data generators, config.py and dotenv
        📁 reports/        → Report directory for test generated reports  
    📁 github/             → YML files for CI application on Github Actions  
    📄 conftest.py          → UI fixtures, like driver and screenshot hook  
    📄 pytest.ini           → Pytest markers and other settings  
    📄 requirements.txt     → Project requirements (needed packages)

## Requirements:
- Python 3.10+
- Google Chrome (Firefox or Edge)
- pip (package installer for python)
- [virtualenv] (optional but recommended)

> Note: This project was developed in PyCharm, but it can be run on any environment compatible with Python.

### How to start:
#### Clone this repository:

git clone https://github.com/MarinaDesojo/TP_Automation_CodigoFacilito/

cd https://github.com/MarinaDesojo/TP_Automation_CodigoFacilito/

#### Create a virtual environment:
##### On Linux/macOS:
python3 -m venv venv

source venv/bin/activate

#### On Windows(cmd):
python -m venv venv

venv\Scripts\activate
 
#### Install packages:

pip install -r requirements.txt

## URLs:
### UI website tested:
https://shophub-commerce.vercel.app/

### API tested:
https://cf-automation-airline-api.onrender.com/


## How to run tests
### To run the tests, go to the project root and:

#### 👉 To run all tests:
- pytest

#### 👉 To run a specific file:
- pytest API_project/tests/users/test_users
- pytest UI_project/tests/test_login_and_sign_up.py

#### 👉 To run a specific test inside a file:
- pytest UI_project/tests/test_login_and_sign_up.py::test_login_wrong_email_11

#### 👉 To run by markers (example: login):
- pytest -m login

#### 👉 To run all website ui tests or all api tests, run:
- pytest -m web
- pytest -m api

#### 👉 To add another marker, for example "e2e", run:
- pytest -m "web and e2e"

#### 👉 Chrome is the default browser used for web tests, in case you want to test on Firefox or Edge, run:
- pytest -m web --browser=firefox
- pytest -m web --browser=edge

#### 👉 To run the test suite headless, add --headless, for example:
- pytest -m web --headless

#### 👉 To generate a report that includes the embedded screenshot from failed tests, run:
- pytest --html=UI_project/reports/{name_of_the_report}.html --self-contained-html
- pytest --html=API_project/reports/{name_of_the_report}.html --self-contained-html

#### 👉 To see on the console (CLI) logs add --log-cli-level=INFO, for example:
- pytest -m web --log-cli-level=INFO

#### All markers:

markers =
- web: UI web related tests
- api: API related tests
- e2e: End to end flow test
- happy_path: Happy path tests
- fail: Fail intended tests
- login: Login flow related tests
- sign_up: Sign un flow related tests
- search: Search flow related tests
- shop: Shop flow related test
- navigation: Navigation related tests
- content_verification: Content like text verification tests
- users: API User endpoint related tests
- airports: API Airports endpoint related tests
- aircrafts: API Aircrafts endpoint related tests
- flights: API Flights endpoint related tests
- bookings: API Bookings endpoint related tests
- payments: API Payments endpoint related tests
