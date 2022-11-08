# Project : POEI HARMONIC

---

## Team
* Ruddy MOUNIAMA MOUNICAN 
* David DONISA 
* Kévin BARDOUX

---
## Project description
As part of a Python training and to put into practice the different modules of the course, we
will create an application that allows:

A developer to submit, via a REST API, code, with technical specifications previously defined,
to test the code and track test results.

To set up this application, you must create a REST API accessible both to the administrators
of the application and to the developers who wish to use the application.

#### The Administrator part must allow:

* To add the technical specifications of the expected functions, as well as the test scripts
associated with each function.
* To consult the code proposals by the developers and their coverage of the tests.

#### The developer part must allow:
* To access the technical specifications of the functionalities to be developed.
* To be able to submit a response to a feature either by a library developed in c, or source
code in python.
* To consult the result of the tests of a response to a specification.
* To consult the response history, with the possibility of having a link to submit a new
proposal if the test coverage is not 100%.
The entire API must be secured using a JWT, and a roles mechanism to distinguish between
users and developers.

## Functional Specifications
### 1 - Registration and login
A user who wishes to use our application must first register using an email, name, first name
and a password.

A user can connect using his email and password, after connection we will distinguish
between administrator and developer.

The administrator is created automatically at the first start of the application, we cannot
have more than one administrator.

### 2 –Features of the administrator.
The application administrator can add a feature to be developed, the feature must have, a
name, a description, the signature of the expected function and a test file developed in
pytest.

Admin can access the list of registered features.

It can also, for each feature, have the list of developers who have sent a response as well as
the response with a ranking by test coverage rate.

### 3 – Features of developers
A developer can access the list of features to be developed, he will have access to the name
of each feature, its description and its signature.
A developer can submit his code to respond to the functionality either in the format of a
Python script, a dll developed in C. “As a bonus, a script in C”
The submission response must contain the link to access the feature test result.
In the case where the coverage is not total, the developer can submit a new response.

## Technical criteria for carrying out the project.
The application must expose the functionalities by a REST API developed in python and
tested by the Pytest framework.

The application must persist the data in a relational database (postgresql or others…).

The application must be covered by unit, integration and functional tests.

## Return of the trainees
Each group must submit:

* A description of the different stages in the creation of the application.

* The source code of the application.

* The different tasks performed and by which member.

* Resources to automate the deployment and execution of tests on multiple environments.

* The results of the various tests.

* A demonstration of the application.


## Idea of this project
* Ihab ABADAI - Utopios