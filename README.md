# BDD in Python Behave

## Overview

The project presents behaviour-driven development (BDD) tests in Python, written
using [Behave](https://behave.readthedocs.io/en/stable/index.html). 

Other technologies used: [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/), [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager).

Tested app is a demo store [SwagLabs](https://www.saucedemo.com/).

## Requirements
* Python 3.10 or higher
* Optional: Git, PyCharm or VSCode with extension that supports BDD

## User stories and test scenarios

Exemplary user stories covers main functionalities of the app. Based on them were written test scenarios
in [Gherkin language](https://behave.readthedocs.io/en/stable/philosophy.html#the-gherkin-language):

- Scenario: (explain scenario).
    - Given (how things begin),
    - when (action taken),
    - then (outcome of taking action).

Scenarios can be found in the feature files as per the table:

| Title             | User story                                                                                            | Test scenarios            | Step definition        |
|-------------------|-------------------------------------------------------------------------------------------------------|---------------------------|------------------------|
| Log into the app  | As a user, <br />I want to be able to log in with registered data <br />so that I can access the app. | feature/login.feature     | feature/steps/login.py |                                                                                                              |                      |                                                   |
| Sort inventory    | As a user, <br />I want to be able to sort items by their names and prices.                           | feature/inventory.feature | feature/steps/store.py |                                                                                                                     |                      |                                                   |
| Manage a cart     | As a user, <br />I want to view the shopping cart, add and remove items.                              | feature/cart.feature      | feature/steps/store.py |
| Checkout an order | As a user, <br />I want to checkout my order<br /> so that I can complete shopping.                   | feature/checkout.feature  | feature/steps/store.py |

## Project structure

Feature files are arranged by business functionality (e.g. `cart.feature` contains all tests related to cart functionality) while step definitions by domain (e.g. `login.py` contains all actions that are done on login screen).

The feature directory has the following structure:

```
features/
features/login.feature
features/inventory.feature
features/cart.feature
features/checkout.feature
features/environment.py
features/steps/
features/steps/login.py
features/steps/store.py
```

## Setup

Clone repository:

```bash
git clone <repo-url>
```

```bash
cd behave-bdd-swaglabs
```

Activate virtual environment:

```bash
python -m venv venv
```

```bash
venv\Scripts\activate.bat
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
behave
```
