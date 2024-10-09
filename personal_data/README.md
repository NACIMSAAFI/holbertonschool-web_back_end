# Curriculum [C#22] Spe - Web Stack Programming 2024

### Description

Hey there! Welcome to my project on web stack programming. In this project, I've dived into handling Personally Identifiable Information (PII) and managing passwords. It’s all about making sure our web applications are secure and user-friendly.

## Resources

Here are some materials I found super helpful:

- [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
- [Logging Documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt Package](https://github.com/pyca/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)

## Learning Objectives

By the end of this project, I want to be able to explain a few key concepts, including:

- What exactly counts as Personally Identifiable Information (PII).
- How to create a log filter that hides PII fields.
- The steps to encrypt a password and check if an input password is valid.
- How to authenticate to a database using environment variables.

## Requirements

Here’s what I need to keep in mind while working on this project:

- I’m using Ubuntu 20.04 LTS with Python 3.9.
- Each of my files needs to end with a new line.
- The first line of all files should be: `#!/usr/bin/env python3`.
- I have to include this `README.md` file at the root of my project.
- My code should follow the `pycodestyle` guidelines (version 2.5).
- All my files must be executable.
- The length of my files will be checked using `wc`.
- Documentation is key! I need to document all my modules, classes, and functions properly.
  - I can verify my documentation with commands like:
    - For modules: `python3 -c 'print(__import__("my_module").__doc__)'`
    - For classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
    - For functions outside classes: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
    - For functions inside classes: `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- Lastly, all my functions should have type annotations.

## Getting Started

If you want to check this out, you can clone the repo and jump into the project directory:

```bash
git clone https://github.com/NACIMSAAFI/holbertonschool-web_back_end.git
cd personal_data
