from typing import Final

from basic import basic
from loguru import logger


def main():
    """Main method. Entry point."""
    try:
        basic(PATH_EMAIL, PATH_JSON)
    except Exception as ex:
        logger.critical('You have done something wrong!', ex)


if __name__ == '__main__':
    PATH_EMAIL: Final = '../files/email/email.csv'
    PATH_JSON: Final = 'https://jsonplaceholder.typicode.com/users/'
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
