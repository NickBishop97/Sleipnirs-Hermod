# Introduction

One of the main deliverables for Hermod DDS is to test the application to verify that requirements have 
been meet to qualify as a viable product. To ensure that the behavior of the application meets the requirements of the product,
the following testing methods and methodolgies have been or will be used:
- BDD and ATDD Testing Methodologies
- Unit Testing
- Static Analysis (Code Coverage and Linting)
- Integration Testing

## BDD and ATDD Testing Methodologies

Explain concepts and frameworks aka Gerkin and Robot/Behave frameworks

Explain the importance and how/why they should be used for Hermod DDS

## Unit Testing

Unit testing ensures that the individual components behave as appropriatly when called upon. Testing the DDS portion is not required as the framework fastDDS has already been tested. Everything else that has been implemented on top of the DDS framework, however, will need to be unit and integrate tested. For unit testing, the following modules are being used for unit testing:

- Pytest (python)

- BOOST (C++)

## Static Analysis (Code Coverage and Linting)

Introduction of static analysis and how/why it is being used for Hermod DDS

### Code Coverage

Explain code coverage and the tools used to find code coverage

- C++

- Python

### Linting

Explain linting and the tools used to lint the code

- C++

- Python


## Integration Testing

Explain concepts of static analysis and how they would like to be used for Hermod DDS

As of 7/29/2022, the following limitations, concerns and questions need to be resolved to practically use integration testing:

1. The need to separate function calls to all subscribers and publishers and place them into a sort of main file rather than calling them at the end file. This is mostly with python, so C++ shouldn't have this kind of problem. This main file could also simplify the process of startup and teardown when running the application.
2. The need to decide how to verify integration. Capture the stdout? Capture instances, storing temp values? As of right now with random gen values being published, we'd need to rewrite or create separate test lists that the publishers could read when testing to control when normal or unexpected behaviors occur.