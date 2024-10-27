# Unit and Integration Tests in Python

This project focuses on implementing **unit tests** and **integration tests** for Python code using the `unittest` framework. Below, you'll find details about the project, its structure, and how to execute the tests.

## Project Description

- **Unit tests** ensure individual functions perform as expected with different input scenarios (standard and edge cases). Any external dependencies like network calls or database operations are mocked.
- **Integration tests** validate that different components of the system work together as expected. Only the low-level functions that make external calls are mocked.

## Learning Objectives

By completing this project, you will:

- Understand the **difference between unit and integration tests**.
- Apply common testing patterns such as **mocking**, **parameterization**, and **fixtures**.
- Gain experience using Python's `unittest` framework and `unittest.mock`.

## Technologies Used

- **Language**: Python 3.9
- **Operating System**: Ubuntu 20.04 LTS
- **Testing Framework**: `unittest`
- **Style Guide**: `pycodestyle` (version 2.5)

## Requirements

- All Python files must be **Python 3.9 compatible**.
- Code must follow **pycodestyle** guidelines.
- Each function, class, and module should have **detailed documentation**.
- All functions must have **type annotations**.

## Project Structure

- `utils.py`: Helper functions used across the project.
- `client.py`: Contains client-related functionality.
- `fixtures.py`: Predefined data used for testing purposes.

## How to Run the Tests

To run the tests, use the following command:

```bash
$ python -m unittest path/to/test_file.py

```

## Additional Resources

unittest — Unit testing framework
unittest.mock — mock object library
parameterized — Python parameterized tests

## Author

Project by Emmanuel Turlay, Staff Software Engineer at Cruise.
