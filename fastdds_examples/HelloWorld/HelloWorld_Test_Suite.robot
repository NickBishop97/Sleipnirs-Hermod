*** Settings ***
Resource        HelloWorld_keywords.resource

*** Variables ***

*** Test Cases ***
Pytest Test Suite
    Given The Pytest File is Running
    And It has Finished Running
    Then The Pytest Should have passed
    