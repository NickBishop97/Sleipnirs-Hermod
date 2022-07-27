# Sleipnir's Hermod Requirements

These are the functional requirements that we created based on the customer wants and needs.

## Functional Requirements
What follows are the functional requirements set by the client, which were later refined and changed.

Number of Topics: 5
Number of Exclusively Publishers: 2
Number of Exclusively Subscribers: 5
Number of Multi-Subscribers and Single Subscribers: 3

**1. System Level Requirements:**

    System:
        - The vehicle shall display a visible indicator to the driver when the vehicle is projected to run out of fuel within 5 liters or less from the Low Fuel Alert Monitor.
        - The vehicle shall display to the driver the amount of fuel remaining in liters from the tank as a percentage from the Fuel Gauge.
        - The vehicle shall display average miles per gallon to the driver from the Miles Per Gallon.
        - The vehicle shall display the selected road trip of miles traveled to the driver from the Road Trip Meter.

**2. Publisher Requirements:**

    Fuel Sensor:
        - The Fuel Sensor shall measure the amount of fuel remaining in liters every 0.25 seconds.
        - The Fuel Sensor shall publish amount of fuel remaining in liters to the Fuel Remaining Topic every 0.25 seconds.
        - The Fuel Sensor shall determine the amount of fuel spent in liters every 0.25 seconds.
        - The Fuel Sensor shall publish the amount of fuel spent in liters to the Fuel Spent Topic every 0.25 seconds

    Button Sensor:
        - The Button Sensor shall read the user input of the amount of time in seconds the button was pushed.
        - The Button Sensor shall publish the button input in seconds to the Road Trip Meter Topic whenever the user inputs.


**3. Subscriber Requirements:**

    Distance Display:
        - The Distance Display shall receive miles traveled from the Miles Traveled Topic.
        - The Distance Display shall always display miles traveled to the dashboard.

    Miles Left Until Refuel:
        - The Miles Left Until Refuel shall receive miles per gallon from the Miles Per Gallon Topic.
        - The Miles Left Until Refuel shall receive fuel remaining from the Fuel Remaining Topic.
        - The Miles Left Until Refuel shall calculate miles remaining using miles per gallon and fuel remaining.
        - The Miles Left Until Refuel shall display miles remaining every 0.25 seconds.

    Miles Per Gallon Monitor:
        - The Miles Per Gallon Monitor shall receive miles per gallon from the Miles Per Gallon Topic.
        - The Miles Per Gallon Monitor shall display miles per gallon of the vehicle every 0.25 seconds.

    Fuel Gauge:
        - The Fuel Gauge shall receive fuel remaining in liters from the Fuel Remaining Topic.
        - The Fuel Gauge will calculate fuel remaining percentage using fuel remaining and tank capacity.
        - The Fuel Gauge shall display fuel remaining percentage every 0.25 seconds.

    Low Fuel Alert Monitor:
        - The Low Fuel Alert Monitor shall receive miles remaining from the Fuel Remaining Topic.
        - The Low Fuel Alert Monitor shall display a Low Fuel Indicator to the Dashboard when the projected fuel remaining is 5 litters or less.
        - Once the Low Fuel Indicator has turned on, the Low Fuel Alert Monitor shall remain on display until the projected Fuel remaining is more than 5 litters.


**4. Pub/Sub Requirements:**

    Miles Per Gallon:
        - Miles Per Gallon shall receive fuel spent in liters from the Fuel Spent Topic.
        - Miles Per Gallon shall receive miles traveled from the Miles Traveled Topic.
        - Miles Per Gallon shall calculate miles per gallon using miles traveled and fuel spent.
        - Miles Per Gallon shall publish miles per gallon to its subscribers every 0.25 seconds.

    Miles Traveled Sensor:
        - The Miles Traveled Sensor shall measure the amount of miles traveled every 0.25 seconds.
        - The Miles Traveled Sensor shall publish miles traveled to the Miles Traveled Topic every 0.25 seconds.
        - The Miles Traveled Sensor shall stop and print its final value after the fuel sensor reaches zero fuel remaining.

    Road Trip Meter:
        - The Road Trip Meter shall receive the amount of miles traveled from the Miles Traveled topic every 0.25 seconds.
        - The Road Trip Meter shall receive the the button input from the Road Trip Meter Topic asynchronously.
        - The Road Trip Meter shall increment the amount of miles traveled onto the miles traveled of Trip 1 and Trip 2.
        - The Road Trip Meter shall publish the trip miles traveled of the currently selected trip number to its subscribers every 0.25 seconds.
        - The Road Trip Meter shall determine from the button input to do either of the following:
            - Reset the trip miles traveled to the trip number that is currently selected.
            - Switch the trip number that is currently being published to its subscribers.


**5. Topic Requirements:**

    Fuel Remaining Topic:
        - The Fuel Remaining Topic shall receive fuel remaining from the Fuel Sensor.
        - The Fuel Remaining Topic shall publish only fuel remaining to its subscribers every 0.25 seconds.

    Fuel Spent Topic:
        - The Fuel Spent Topic shall receive fuel spent from the Fuel Sensor.
        - The Fuel Spent Topic shall publish fuel spent to its subscribers every 0.25 seconds.

    Miles Remaining Topic:
        - The Miles Traveled Topic shall receive miles traveled from the Miles Sensor.
        - The Miles Traveled Topic shall publish only miles traveled to its subscribers every 0.25 seconds.

    Miles Per Gallon Topic:
        - The Miles Traveled Topic shall receive miles traveled from the Miles Sensor.
        - The Miles Traveled Topic shall publish only miles traveled to its subscribers every 0.25 seconds.

    Miles Per Gallon Topic:
        - The Miles Per Gallon Topic shall receive miles per gallon from the Miles Per Gallon.
        - The Miles Per Gallon Topic shall publish miles per gallon to its subscribers.

    Road Trip Meter Topic:
        - The Road Trip Meter Topic shall receive the button input from the Button Sensor.
        - The Road Trip Meter Topic Topic shall publish the button input to its subscribers.

## Design Constraints

What follows are the design constraints determined by the team to carry out the functional requirements.

**Fuel Sensor Implementation Requirements:**

    Fuel Sensor shall send:
        - Message Index (unsigned integer)
        - Liters Remaining (double)
        - Liters Spent (double)
    Fuel Sensor shall force other sensors to read 0.0 for none index values until it Fuel Sensor start.

**Miles Sensor Implementation Requirements:**

    Miles Traveled Sensor shall send:
        - Message Index (unsigned integer)
        - Cumulative Miles Traveled (double)

**Miles Per Gallon Implementation Requirements:**

    Miles Per Gallon shall send:
        - Message Index (unsigned integer)
        - Cumulative Miles Per Gallon (double)

**Miles Left Until Refuel Implementation Requirements:**

    Miles Left Until Refuel shall send:
        - Message Index (unsigned integer)
        - Miles Left Until Refuel (double)

**Low Fuel Alert Monitor Implementation Requirements:**

    Low Fuel Alert Monitor shall send:
        - Message Index (unsigned integer)
        - Is Fuel Low (signed integer) (treat as bool)

**Road Trip Meter Implementation Requirements:**

    Button Sensor shall send:
        - Message Index (unsigned integer)
        - Button Pressed in seconds (unsigned integer)
    Road Trip shall send:
        -The current trip number being displayed (string) (i.e. Trip #)
        - Road Trip of miles traveled (unsigned integer)

**Standard Protocol:**

    Subscribers:
        - When a Subscriber disconnects: A Publisher will continue writing even if there were no initial Subscribers.
    Publishers:
        - When a Publisher disconnects: a Subscriber will contnue to read an error value even if there were no initial Publishers.
            - For the double value, it will be -1.0
            - For the integer value, it will be -1