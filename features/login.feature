Feature: Log into the app
  As a user
  I want to be able to log in with registered data
  so that I can access the app.


  Scenario Outline: Login with valid data
    Given user is on Login page
    When user enters <username> as Username
    And user enters <password> as Password
    And user clicks "Login" button
    Then user is navigated to "All Items" page
    Examples:
      | username      |  | password     |
      | standard_user |  | secret_sauce |

  Scenario Outline: Login with invalid data
    Given user is on Login page
    When user enters <username> as Username
    And user enters <password> as Password
    And user clicks "Login" button
    Then notification <notification> is thrown
    And user is not logged into the app
    Examples:
      | username      |  | password     |  | notification                                                              |
      | Standard_user |  | secret_sauce |  | Epic sadface: Username and password do not match any user in this service |
      | standard_user |  | secret_Sauce |  | Epic sadface: Username and password do not match any user in this service |
      | NULL          |  | NULL         |  | Epic sadface: Username is required                                        |
      | NULL          |  | secret_sauce |  | Epic sadface: Username is required                                        |
      | standard_user |  | NULL         |  | Epic sadface: Password is required                                        |


