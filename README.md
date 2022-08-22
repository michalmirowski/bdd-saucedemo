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

| Title             | User Story                                                                                                               | Acceptance criteria      | Step implementation                               |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------|---------------------------------------------------|
| Log into the app  | As a user, <br />I want to be able to log in with registered data <br />so that I can access the app.                    | feature/login.feature    | tbd                                               |                                                                                                              |                      |                                                   |
| Browse items      | As a user, <br />I want to be able to sort items on their names and prices <br />so that I can find what I need quicker. | feature/browse.feature   | tbd                                               |                                                                                                                     |                      |                                                   |
| Manage a cart     | As a user, <br />I want to view the shopping cart, add and remove items<br /> so that I can manage my cart.              | feature/cart.feature     | feature/steps/common.py<br/>feature/steps/cart.py |
| Checkout an order | As a user, <br />I want to checkout my order<br /> so that I can complete shopping.                                      | feature/checkout.feature | tbd                                               |

  
