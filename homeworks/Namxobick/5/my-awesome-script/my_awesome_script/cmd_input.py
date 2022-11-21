import argparse

from .command import command, functions


def cmd_input():
    """Input method."""
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', help='Input command', choices=functions)
    parser.add_argument('parameter', help="'Any text' or 'Region/City'")
    args = parser.parse_args()

    try:
        command(args.operation, args.parameter)
    except Exception as ex:
        command('help')
        raise ex
