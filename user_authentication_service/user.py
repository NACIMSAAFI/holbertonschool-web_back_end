#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(250), nullable=False)
    user_hashed_password = Column(String(250), nullable=False)
    user_session_id = Column(String(250), nullable=True)
    user_reset_token = Column(String(250), nullable=True)
