#! /usr/bin/env python3
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(
        prog='Zoo Manager Command-Line Utility',
        description='Manages zoo files containing animal data'
    )
    parser.add_argument('-f', '--file', help='Name of the zoo file to modify.', default='zoo_data.txt')

    subparsers = parser.add_subparsers(help='SUBCOMMANDS')

    list_parser = subparsers.add_parser('list', help='Lists all animals in the zoo file.')

    add_parser = subparsers.add_parser('add', help='Adds a new animal to the zoo file.')
    add_parser.add_argument('name', help='Name of the individual animal.')
    add_parser.add_argument('type', help='Type of animal to add.', choices=['cat','dog','bird'])

    remove_parser = subparsers.add_parser('remove', help='Remove an animal by name OR remove animals by type.')
    remove_parser.add_argument('-n', '--name', help='Name of the individual animal.')
    remove_parser.add_argument('-t', '--type', help='Type of animal to add.', choices=['cat','dog','bird'])

    arguments = parser.parse_args()
    print(arguments)
else:
    print("It looks like you've imported the executable script from elsewhere in the codebase!  Please ensure you only call this script from the command line.")