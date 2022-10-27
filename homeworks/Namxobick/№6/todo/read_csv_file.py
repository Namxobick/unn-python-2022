import csv

from loguru import logger


def read(path: str = None) -> tuple:
    """
    Read the csv file.

    :param path :path to email.csv
    :return tuple : tuple of emails
    """
    with open(path) as csv_file:
        emails: list[str] = []
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for line in reader:
            emails.extend(line)

        logger.info('{0} users were read from csv file'.format(len(emails)))
        return tuple(emails)
