#!/usr/bin/env python3
"""Authentication"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with an email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            User: The created user instance.

        Raises:
            ValueError: If a user with the same email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)

        user = User(email=email, hashed_password=hashed_password)
        self._db.add_user(email, hashed_password)

        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a user's login.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            bool: True if login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            pw_bytes = password.encode("utf-8")
            match = bcrypt.checkpw(pw_bytes, user.hashed_password)
            return match
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """Generate a UUID and return its string representation."""
        return str(uuid.uuid4())
