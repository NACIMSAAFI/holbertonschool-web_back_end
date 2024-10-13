#!/usr/bin/env python3
""" Hashing Password """

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password with bcrypt and returns the hashed password."""
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
