*** Settings ***
Resource        HelloWorld_keywords.resource

*** Variables ***

*** Test Cases ***
Test Publisher and Consumer
    Given The Subscriber Is Running
    When The Publisher Connects To The Topic
    And The Publisher Has Stopped Running
    Then The Publisher Finished Sending Data
    