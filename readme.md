to make venv
python -m venv venv
to activate venv
venv\Scripts\activate
Install playwright with pytest
pip install pytest-playwright
it install all browsers binary
playwright install
Run tests
pytest test
Run tests with browser
pytest test --browser=chromium
Run tests in parallel
playwright test --workers=2
Run tests with browser and parallel
playwright test --browser=chromium --workers=2
Run tests with browser and parallel and report
playwright test --browser=chromium --workers=2 --reporter=dot
playwright codegen
playwright codegen https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
pytest test
pytest test