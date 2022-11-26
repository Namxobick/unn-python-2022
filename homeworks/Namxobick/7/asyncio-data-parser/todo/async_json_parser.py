import asyncio

import httpx
from loguru import logger


def get_all_info(path: str) -> dict:
    """
    Gets all the information from the website.

    :param path : path PATH_JSON
    :return dict : information from the website
    """
    response = httpx.get(path)
    return response.json()


async def get_email_id(path: str) -> dict:
    """
    Receives the user ID by email from the website.

    :param path : path PATH_JSON
    :return dict : email:id
    """
    logger.info('The beginning of requests users from the site')
    user_email_id: dict[str:int] = {}
    async with httpx.AsyncClient() as client:
        response = await client.get(path)

    users_info = response.json()
    for user_info in users_info:
        user_email_id[user_info.get('email')] = user_info.get('id')

    logger.info('The ending of requests users from the site: took {0}'.format(
        response.elapsed,
    ))
    logger.info('Users: {0}'.format(user_email_id))
    return user_email_id


async def get_user_info(path: str, user_id: str, types_info: list) -> dict:
    """
    Receives the user info ('posts', 'albums', 'todos') by id from the website.

    :param path : path PATH_JSON
    :param user_id
    :param types_info : ['posts', 'albums', 'todos']
    :return dict : email:id
    """
    user_info: dict[str:list] = {}
    logger.info('Starts parsing for ID: {0}'.format(user_id))
    users_type_info = await asyncio.gather(*(
        _get_user_type_info(type_info, path, user_id)
        for type_info in types_info
    ))
    for user_type_info in users_type_info:
        user_info[user_type_info[0]] = user_type_info[1]

    logger.info('Ends parsing for ID: {0}'.format(user_id))
    return user_info


async def _get_user_type_info(type_info: str, path: str, user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(path + '{0}/{1}/'.format(
            user_id,
            type_info,
        ))
        logger.info(('Request to ID: {1} for get {0}: took {2}'.format(
            type_info,
            user_id,
            response.elapsed,
        )))
    return type_info, response.json()