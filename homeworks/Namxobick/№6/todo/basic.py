import re

import json_parsing as scraping
import read_csv_file as csv
from loguru import logger
from writer_xml import write_xml


def basic(path_email: str, path_json: str):
    """
    Basic method.

    Connects other methods.

    :param path_email : path to PATH_EMAIL
    :param path_json : path to PATH_JSON
    """
    types_info = ['posts', 'albums', 'todos']
    _user_xml(types_info, path_email, path_json)


def _is_email(entry: str) -> bool:
    regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.match(regex, entry) is not None


def _get_emails_id(path_email: str, path_json: str) -> dict:
    all_emails_id = scraping.get_email_id(path_json)
    emails = csv.read(path_email)

    emails_id = {}
    for key in emails:
        if _is_email(key):
            user_id = all_emails_id.get(key)
            if user_id is None:
                logger.warning('{0} missing from the website'.format(key))
            else:
                emails_id[key] = user_id
        else:
            logger.warning('{0} is not valid email'.format(key))
    logger.info('{0} users were found in website'.format(len(emails_id)))
    return emails_id


def _user_xml(types_info: list, path_email: str, path_json: str):
    emails_id = _get_emails_id(path_email, path_json)
    for key in emails_id:
        path = '../files/users/{0}.xml'.format(str(emails_id.get(key)))
        user_id = str(emails_id.get(key))
        user_info = scraping.get_user_info(path_json, user_id, types_info)
        write_xml(user_id, str(key), user_info, types_info, path)
