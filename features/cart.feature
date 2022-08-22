Feature: Managing a cart
  As a user
  I want to view the shopping cart, add and remove items
  In order to control my order

  Background: Preparing the app
    Given user is logged in
    And app is reset

  Scenario: Open empty cart
    Given user is on "All Items" page
    When user clicks cart icon
    Then cart is opened
    And cart is empty


  Scenario Outline: Add items to a cart
    Given user is on "All Items" page
    When user adds <number> item(s) to cart
    And user clicks cart icon
    Then cart is opened
    And in the cart is <number> item(s)
    Examples:
      | number |
      | 1      |
      | 5      |

  Scenario: Remove items from a cart
    Given cart with some items is opened
    When user clicks "Remove" button
    Then item is removed


