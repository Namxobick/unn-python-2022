from typing import Final

import asyncio_
import multiprocessing_
import single_threaded
import thread_pool_executor
import threading_


def main():
    """Main method. Entry point."""
    try:
        print(single_threaded.test_request(PATH))
        print(threading_.test_request(PATH))
        print(thread_pool_executor.test_request(PATH))
        print(multiprocessing_.test_request(PATH))
        print(asyncio_.test_asyncio(PATH))

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    PATH: Final = list(map(lambda x: 'https://jsonplaceholder.typicode.com/users/' + str(x), range(1, 11)))
    try:
        main()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
