*** Settings ***
Resource         MilestoDash_keywords.resource

*** Keywords ***
Pytest
    Given The miles publisher is started
    And The dashboard is started