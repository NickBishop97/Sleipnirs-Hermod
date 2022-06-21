*** Settings ***
Library    Process
Library    String

*** Keywords ***
The Subscriber Is Running
    Log To Console   Opening Subscriber
    Start Process    python3    HelloWorldSubscriber.py    alias=Sub

The Publisher Connects To The Topic
    Log To Console   Opening Publisher
    Start Process    python3    HelloWorldPublisher.py    alias=Pub

The Publisher Has Stopped Running
    Sleep    10
    ${var1}=    Is Process Running    Pub
    IF    ${var1}
        Log To Console    Pub not stopped
        Fail    Publisher still running
    ELSE
        Log To Console    Sub stopped
        Terminate Process    Sub
        Terminate Process    Pub
        ${result}=    Get Process Result    Pub
        Log To Console    ${result.stdout}
    END

The Publisher Finished Sending Data
    ${result}=    Get Process Result    Pub
    ${line}=    Get Lines Containing String    ${result.stdout}    Sending Hello World : 9
    Log To Console    ${line}
    IF    "${line}" == "Sending Hello World : 9"
        Pass Execution    Publisher Completed Task
        Log To Console    ${correct}
    ELSE
        Fail    Publisher didn't complete Task
        Log To Console    ${correct}
    END
