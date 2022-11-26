from datetime import datetime
from multiprocessing import Process

import httpx


def _worker(path_user: str):
    httpx.get(path_user)


def test_request(paths: list[str]):
    start_time = datetime.now()
    processes = []
    for path_user in paths:
        process = Process(target=_worker, args=(path_user,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return datetime.now() - start_time
