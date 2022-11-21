
from .cmd_input import cmd_input


def main():
    """Main method."""
    try:
        cmd_input()
    except Exception as ex:
        print('You have done something wrong!', ex)  # noqa: WPS421


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()  # noqa: WPS421
        print('Shutting down, bye!')  # noqa: WPS421
