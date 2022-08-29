Feature: Checkout an order
  As a user
  I want to checkout my order
  so that I can complete shopping.

  Background: Preparing the app
    Given user is logged in
    And app is reset

  Scenario Outline: Checkout order with valid information
    Given cart with some items is opened
    When user clicks "Checkout" button
    And user enters <first_name> as a First Name
    And user enters <last_name> as a Last Name
    And user enters <postal_code> as a Zip/Postal Code
    And user clicks "Continue" button
    Then user is navigated to "Checkout: Overview" page
    And total is a sum of items amounts and taxes

    Examples:
      | first_name | last_name | postal_code |
      | John       | Doe       | AL19YG      |


  Scenario Outline: Checkout order with invalid information
    Given cart with some items is opened
    When user clicks "Checkout" button
    When user enters <first_name> as a First Name
    And user enters <last_name> as a Last Name
    And user enters <postal_code> as a Zip/Postal Code
    And user clicks "Continue" button
    Then checkout warning is thrown: <notification>
    And user stays on "Checkout: Your Information" page

    Examples:
      | first_name | last_name | postal_code | notification                   |
      | NULL       | NULL      | NULL        | Error: First Name is required  |
      | NULL       | Doe       | AL19YG      | Error: First Name is required  |
      | John       | NULL      | AL19YG      | Error: Last Name is required   |
      | John       | Doe       | NULL        | Error: Postal Code is required |

    Scenario: Complete shopping
      Given user is on "Checkout: Overview" page
      When user clicks "Finish" button
      Then checkout is completed

