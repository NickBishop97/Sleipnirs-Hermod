*** Settings ***
Library    Process
Library    String
Library    XML

*** Keywords ***
The Pytest File is Running
    Log    Opening Pytest.py
    Start Process     pytest    -s    test_HelloWorld.py    alias=Test

It has Finished Running
    Sleep    10
    ${var1}=    Is Process Running    Test
    IF    ${var1}
        Log To Console    Pytest is still Running after 10 secs
        Fail    Pytest still running
    ELSE
        Log To Console    Test Stopped
        Terminate Process    Test
    END

The Pytest Should have passed
    ${result}=    Get Process Result    Test
    ${pass}=    Evaluate    "passed" in """${result.stdout}"""
    ${fail}=    Evaluate    "failed" in """${result.stdout}"""
    ${error}=    Evaluate    "error" in """${result.stdout}"""
    IF    ${fail}
        Fail    Pytest Failed
        Log    ${result.stdout}
    ELSE IF    ${pass}
        Log    ${pass}
        Log    ${result.stdout}
    ELSE IF    ${error}
        Log    ${result.stdout}
        Fail    Pytest has Thrown and error
    ELSE
        Fail    Pass or Fail not found
    END