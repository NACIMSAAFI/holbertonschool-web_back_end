#!/usr/bin/env python3
"""SQLAlchemy model named User for a database table
named users (using the mapping declaration of SQLAlchemy)"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """Represents a user in the users table.

    Attributes:
        user_id (int): The primary key for the user.
        user_email (str): The email of the user;
        must be unique and non-nullable.
        user_hashed_password (str): The hashed password of the user;
        must be non-nullable.
        user_session_id (str): An optional session ID for the user.
        user_reset_token (str): An optional reset token for password recovery.
    """
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(250), nullable=False)
    user_hashed_password = Column(String(250), nullable=False)
    user_session_id = Column(String(250), nullable=True)
    user_reset_token = Column(String(250), nullable=True)
