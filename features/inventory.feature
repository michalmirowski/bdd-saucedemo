Feature: Sort inventory
  As a user
  I want to be able to sort items by their names and prices

  Background: Preparing the app
    Given user is logged in
    And app is reset

  Scenario Outline: Sort by names or prices
    Given user is on "All Items" page
    When user expands sort dropdown
    And user chooses <sort_option> option
    Then items are displayed in <order_type>
    Examples:
      | sort_option         | order_type                   |
      | Names (A to Z)      | alphabetical order           |
      | Names (Z to A)      | reversed alphabetical order  |
      | Price (low to high) | order by price (low to high) |
      | Price (high to low) | order by price (high to low) |



