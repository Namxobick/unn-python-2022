
from datetime import datetime

import pytz
from cowpy import cow
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer


def command(operation: str, text: str = None) -> None:
    """Function selection."""
    if operation == 'help':
        functions[operation]()
    else:
        functions[operation](text)


def highlights(code: str) -> None:
    """Highlight."""
    print(highlight(code, PythonLexer(), TerminalFormatter()))  # noqa: WPS421


def cowsay(text: str) -> None:
    """Cowsay."""
    print(cow.milk_random_cow(text))  # noqa: WPS421


def time(timezone: str) -> None:
    """Time."""
    local_date = datetime.now(pytz.timezone(timezone))
    print('{0} {1}'.format(local_date.date(), local_date.time()))  # noqa: WPS421


def custom_help() -> None:
    """Help."""
    print('EXAMPLE COMMAND:')  # noqa: WPS421
    print(" highlight 'any text'")  # noqa: WPS421
    print(" cowsay 'any text'")  # noqa: WPS421
    print(" time 'Region/City' (example: Europe/Moscow)")  # noqa: WPS421


functions = {'highlight': highlights, 'cowsay': cowsay, 'time': time, 'help': custom_help}
