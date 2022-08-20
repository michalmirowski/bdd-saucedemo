Feature: Opening a cart
  As a user
  I want to be be able to open a cart
  In order to see what and how many items I'm ordering

  Scenario: Open empty cart
    Given user is logged in
    And app state is reset
    When user clicks cart icon
    Then cart is opened
    And cart is empty


  Scenario Outline: Open not empty cart
    Given user is logged in
    And app state is reset
    When user add <number> items to cart
    And user clicks cart icon
    Then cart is opened
    And there is <number> item(s)
    Examples:
      | number |
      | 1      |
      | 5      |

