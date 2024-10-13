#!/usr/bin/env python3
"""
Filtered logger for user data.
"""
from typing import List
import logging
import re
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """Obfuscate specified fields in the log message."""
    for field in fields:
        message = re.sub(
            rf"{re.escape(field)}=.*?{re.escape(separator)}",
            f"{field}={redaction}{separator}",
            message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """Uses 'filter_datum' to redact the PII fields in a record message."""
    REDACTION = "***"
    FORMAT = "[USER_DATA] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """Returns the formatted log message filtered to censor sensitive
        information."""
        formatted_msg: str = super().format(record)
        return filter_datum(
                self.fields,
                self.REDACTION,
                formatted_msg,
                self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Returns a configured logger object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Function to get a connection to the MySQL Database."""
    try:
        dbUser = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
        dbPass = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
        dbHost = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
        dbName = os.getenv("PERSONAL_DATA_DB_NAME")

        if not dbName:
            raise ValueError("Environment variable is not set.")

        dbConnection = mysql.connector.connect(
            user=dbUser,
            password=dbPass,
            host=dbHost,
            database=dbName
        )

        if dbConnection.is_connected():
            return dbConnection
        else:
            raise ConnectionError("Failed to connect to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def main() -> None:
    """ Main function to fetch and log user data. """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    for row in cursor:
        log_message = (
            f"name={row[0]}; email={row[1]}; phone={row[2]}; "
            f"ssn={row[3]}; password={row[4]}; ip={row[5]}; "
            f"last_login={row[6]}; user_agent={row[7]};"
        )
        logger.info(log_message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
