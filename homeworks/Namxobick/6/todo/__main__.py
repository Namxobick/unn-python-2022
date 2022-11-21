from datetime import datetime
from typing import Final

from basic import basic
from loguru import logger


def main():
    """Main method. Entry point."""
    start_time = datetime.now()
    try:
        basic(PATH_EMAIL, PATH_JSON)
    except Exception as ex:
        logger.critical('You have done something wrong!', ex)
    end_time = datetime.now()
    logger.info('Took {0}'.format(end_time - start_time))


if __name__ == '__main__':
    PATH_EMAIL: Final = '../files/email/email.csv'
    PATH_JSON: Final = 'https://jsonplaceholder.typicode.com/users/'
    try:
        main()
    except KeyboardInterrupt:
        logger.critical('Shutting down, bye!')
