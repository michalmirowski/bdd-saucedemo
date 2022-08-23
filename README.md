# BDD in Python Behave

## Overview

The project presents behaviour-driven development (BDD) tests in Python, written
using [Behave](https://behave.readthedocs.io/en/stable/index.html).

Tested app is demo store  [SwagLabs](https://www.saucedemo.com/).

## Setup

Make sure you have the latest version of Python installed.

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

## User Stories and Implementation

Acceptance criteria for User Stories were written in [Gherkin language](https://behave.readthedocs.io/en/stable/philosophy.html#the-gherkin-language): 
- Scenario: (explain scenario). 
  - Given (how things begin), 
  - when (action taken), 
  - then (outcome of taking action).

Feature files are grouped by business functionality and step definitions by domains so the feature directory has the following structure:

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

| Title             | User Story                                                                                                               | Acceptance criteria       | Step implementation    |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------|
| Log into the app  | As a user, <br />I want to be able to log in with registered data <br />so that I can access the app.                    | feature/login.feature     | feature/steps/login.py |                                                                                                              |                      |                                                   |
| Sort inventory    | As a user, <br />I want to be able to sort items on their names and prices <br />so that I can find what I need quicker. | feature/inventory.feature | feature/steps/store.py |                                                                                                                     |                      |                                                   |
| Manage a cart     | As a user, <br />I want to view the shopping cart, add and remove items<br /> so that I can manage my cart.              | feature/cart.feature      | feature/steps/store.py |
| Checkout an order | As a user, <br />I want to checkout my order<br /> so that I can complete shopping.                                      | feature/checkout.feature  | feature/steps/store.py |

  
