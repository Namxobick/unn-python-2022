from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import httpx


def test_request(paths: list[str], number_threads=10):
    start_time = datetime.now()
    with ThreadPoolExecutor(number_threads) as executor:
        executor.map(httpx.get, paths)
    return datetime.now() - start_time
