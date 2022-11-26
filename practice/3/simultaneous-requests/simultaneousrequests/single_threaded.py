from datetime import datetime

import httpx


def test_request(paths: list[str]):
    start_time = datetime.now()
    for path_user in paths:
        httpx.get(path_user)
    return datetime.now() - start_time
