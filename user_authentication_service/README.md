# Curriculum Overview
## [C#22] Spe - Web Stack Programming 2024

---

### Master
**Created by:** Emmanuel Turlay, Staff Software Engineer at Cruise  
**Project Weight:** 1  
---

## Project Description

This project serves as an educational tool to explore the implementation of a user authentication system. While it’s recommended to use established libraries or frameworks in production, this exercise will take you through the process step-by-step.

---

## Resources

Refer to the following materials for guidance:

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Requests Module](https://docs.python-requests.org/en/master/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## Learning Goals

- Declare API routes in a Flask application
- Handle cookies in web applications
- Retrieve and manage request form data
- Return appropriate HTTP status codes

---

## Requirements

- **Allowed Editors:** vi, vim, emacs
- All code will run on **Ubuntu 20.04 LTS** using **python3** (version 3.9)
- Ensure all files end with a new line
- The first line of each file must be `#!/usr/bin/env python3`
- A `README.md` file is required at the project root
- Follow **pycodestyle** standards (version 2.5)
- Utilize **SQLAlchemy** for database interactions
- All scripts must be executable
- File lengths will be checked using `wc`
- Documentation is required for all modules, classes, and functions
- Each function must have type annotations
- The Flask app should only interact with the **Auth** class, not directly with the database
- Access only public methods from **Auth** and **DB** outside of these classes

---

## Installation

To set up the project, install the **bcrypt** library:

```bash
pip3 install bcrypt
