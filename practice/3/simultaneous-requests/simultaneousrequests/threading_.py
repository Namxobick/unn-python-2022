import threading
from datetime import datetime

import httpx


def _worker(path_user: str):
    httpx.get(path_user)


def test_request(paths: list[str]):
    start_time = datetime.now()
    threads = []
    for path_user in paths:
        thread = threading.Thread(target=_worker, args=(path_user,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return datetime.now() - start_time
