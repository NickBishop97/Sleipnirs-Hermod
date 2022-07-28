Feature: unit testing with behave

  Scenario: unit test low fuel
    Given fuel domain is running
    When low fuel receives negative fuel
    Then low fuel should return an error code