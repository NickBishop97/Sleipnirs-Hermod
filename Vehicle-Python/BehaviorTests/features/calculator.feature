Feature: Determining MPG

    Scenario: Negative MPG
        Given the Fuel Sensor, Miles Sensor, and Low Fuel is running
        When the Fuel receives negative miles
        Then the Fuel will return an error code