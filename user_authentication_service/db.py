#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


from user import Base
from user import User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The created user instance.
        """
        user = User(email=email, hashed_password=hashed_password)

        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds the first row in the 'users' table
        that matches the 'kwargs'.

        Then, returns the row as a User object.

        If the 'kwargs' don't match the definition of 'User',
        this method raises 'InvalidRequestError'.

        If no matching 'User' row is found,
        this method raises 'NoResultFound'.
        """
        RESULT: Union[User, None] = (
            self._session.query(User).filter_by(**kwargs).first()
        )

        if RESULT is None:
            raise NoResultFound

        return RESULT
