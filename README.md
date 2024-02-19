## Test task for QA Cloud Camp

The results of the test assignment should be published on GitHub and sent by email before 23:59:59 on June 18, 2023. The practical task consists of several parts, and even if you managed to solve only one part of the task, send it for review.

## Automated API Testing. Part 1

Prepare a project with automated tests that will verify the functionality of all API endpoints described below.

### Technical requirements:

- API url https://jsonplaceholder.typicode.com/
- Methods to be tested: GET /posts, POST /posts, DELETE /posts
- Methods may accept parameters userId, id, title, body
- Use Python as the programming language
- Include instructions in the README on how to set up the project
- Utilize the requests library and pytest


## Automated API Testing. Part 2

Write a Dockerfile for your application that tests the API methods from Part 1.

### Technical requirements:
- Include a run command in the README.
  
---

## Automated API Testing. Part 2. Project Launch without Docker

#### Setup:

- Clone the repository to your computer.

- Navigate to the project's root folder.

- Create a virtual environment:
  ```
  python -m venv venv
  ```

- Activate the virtual environment:
  ```
  python3 -m venv venv source venv/bin/activate
  ```

#### Dependencies:

- Install the dependencies:
  ```
  pip install -r requirements.txt
  ```

#### Running Automated Tests:

- Execute the command to run the tests:
  ```
  pytest -s -v
  ```

#### Generating and Running Allure Reports:

- Execute the command to run the tests:
  ```
  pytest -s -v --alluredir allure-results
  ```

- Execute the command to view the report:
  ```
  allure serve allure-results
  ```
