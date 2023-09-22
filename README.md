# Basics in Python

**Python Basic Functionalities**

## Python CLI

- `python3 -m venv .venv` : create virtual environment.
- `.venv\Scripts\activate` : run virtual environment.
- `pip install -r requirements.txt` : install all the required packages.
- `pip freeze > requirements.txt` : save packages if any new are added.

### Flask Server

- Flask is used for making a server in python. We can use CRUD operations in Flask along with Flask API package.
- **Flask Test**
  - `flask --app feature\flask_api\flask_test run --debug` : this will run `flask_test.py` file. Can open the CLI generated link in browsers.
- Please check the [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/installation/) for more information.
