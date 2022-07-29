# Introduction

One of the main deliverables for Hermod DDS is to test the application to verify that requirements have 
been meet to qualify as a viable product. To ensure that the behavior of the application meets the requirements of the product,
the following testing methods and methodolgies have been or will be used:
- BDD and ATDD Testing Methodologies
- Unit Testing
- Static Analysis (Code Coverage and Linting)
- Integration Testing

## BDD and ATDD Testing Methodologies

Behavior Driven Development and Acceptance Test Driven Development are testing methodologies that focus on creating the necessary tests to validate a product first before implementing it. These methodologies look to validate the requirements and behavior of what a product should do under any given circunstance and not how it should do it.

Two common BDD testing frameworks are Behave and Robot Framework which use gherkin to write out test cases of Given, When, And, and Then. These frameworks are also something we'd like to use for our testing on this project as they allow for html generation of test results, making documentation easier to report any results.

- Robot Framework Documentation:https://robotframework.org/
- Behave Framework Documentation: https://behave.readthedocs.io/en/stable/

## Unit Testing

Unit testing ensures that the individual components behave as appropriatly when called upon. Testing the DDS portion is not required as the framework fastDDS has already been tested. Everything else that has been implemented on top of the DDS framework, however, will need to be unit and integrate tested. For unit testing, the following modules are being used for unit testing:

- Pytest: (Python) Pytests are found under the dir "sleipnir/Vehicle-Python/Pytests".
- https://docs.pytest.org/en/7.1.x/

- BOOST: (C++) BOOST tests are found under the dir "sleipnir/Vehicle-C++/Vehicle/src/Unit_Testing"
- https://www.boost.org/doc/libs/1_43_0/libs/test/doc/html/utf.html
 
You can run all unit tests at once with the sh script unit-test.sh, by group under their dir, or executing the individual file. For specific questions on pytest or boost implementation, refer to their documentation or the setup/how-to run documentation in the README.md.


## Static Analysis (Code Coverage and Linting)

Static Analysis for Project Hermod DDS is to ensure that the integrity and coding standards of the product are maintained. This includes using two main static analysis tools of code coverage and linting. Code coverage to verify what percentage of code is being tested and linting to fix formating and use cases.

### Code Coverage

The following commands are being used for code coverage under unit-test.sh:

- C++: Boost "-ftest-coverage"

- Python: gcov "--cov-report term-missing --cov=Calculators"

### Linting

The following tools are being used for linting (see lint.sh):

- C++: cppcheck

- Python: flake8


## Integration Testing

Integration testing for Project Hermod is to verify that the components within or across the Car's system domain behaves as intented when ran together.

Initally, we tried to integrate test using robot framework. However, as of 7/29/2022, there is a current open issue where threading does not work with robot framework. We also considered mocking, but given that fastDDS has already been tested, mocking as a form of testing for the other components does not make sense nor is practical as a form of verfication for integration testing.

Most recently, we are looking into using the behave framework to create integratation tests as behave's framework, in its tutorial, seems capable of handling threading which is a key component required to run inetgratation tests for a DDS. This has not been verified, as behave is commonly used as a BDD framework for web developments with testing tools such as Selenium. At the moment, a behave test has been written for Project Hermod DDS on the python code base for unit testing as a proof of concept under dir "sleipnir/Vehicle-Python/BehaviorTests/features/steps/calculator_steps.py". More issues and questions need to be resolved before it is worth attempting to create a integrated test using the behave framework.

As of 7/29/2022, the following limitations, concerns and questions need to be resolved to practically use integration testing:

1. The need to separate function calls to all subscribers and publishers and place them into a sort of main file rather than calling them at the end file. This is mostly with python, so C++ shouldn't have this kind of problem. This main file could also simplify the process of startup and teardown when running the application.
2. The need to decide how to verify integration. Capture the stdout? Capture instances, storing temp values? As of right now with random gen values being published, we'd need to rewrite or create separate test lists that the publishers could read when testing to control when normal or unexpected behaviors occur.