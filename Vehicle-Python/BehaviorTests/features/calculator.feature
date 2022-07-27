Feature: unit testing with behave

  Scenario: unit test low fuel
     Given we have fuel domain
      When low fuel receives negative fuel
      Then low fuel should return an error code