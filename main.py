#! /usr/bin/env python3
from argparse import ArgumentParser

def list_animals(args):
    file = args.file
    print('zoo = file_manager.load(', file, ')')
    print('for animal in zoo.get_animals():')
    print('    print(str(animal))')

def add_animal(args):
    file = args.file
    name = args.name
    type = args.type
    print('zoo = file_manager.load(', file, ')')
    print('animal = Animal(', name, type, ')')
    print('zoo.add_animal(animal)')
    print('file_manager.save(zoo)')

def remove_animal(args):
    file = args.file
    name = args.name
    type = args.type
    print('zoo = file_manager.load(', file, ')')
    if name:
        print('zoo.remove_animal(',name,')')
    elif type:
        print('zoo.remove_animal(',type,')')
    print('file_manager.save(zoo)')

if __name__ == "__main__":
    parser = ArgumentParser(
        prog='Zoo Manager Command-Line Utility',
        description='Manages zoo files containing animal data'
    )
    parser.add_argument('-f', '--file', help='Name of the zoo file to modify.', default='zoo_data.txt')
    subparsers = parser.add_subparsers(help='SUBCOMMANDS')

    list_parser = subparsers.add_parser('list', help='Lists all animals in the zoo file.')
    list_parser.set_defaults(func=list_animals)

    add_parser = subparsers.add_parser('add', help='Adds a new animal to the zoo file.')
    add_parser.add_argument('name', help='Name of the individual animal to add.')
    add_parser.add_argument('type', help='Type of animal to add.', choices=['cat','dog','bird'])
    add_parser.set_defaults(func=add_animal)

    remove_parser = subparsers.add_parser('remove', help='Remove an animal by name OR remove animals by type.')
    remove_parser.add_argument('-n', '--name', help='Name of the individual animal to remove.')
    remove_parser.add_argument('-t', '--type', help='Type of animals to remove.', choices=['cat','dog','bird'])
    remove_parser.set_defaults(func=remove_animal)

    arguments = parser.parse_args()

    arguments.func(arguments)
else:
    print("It looks like you've imported the executable script from elsewhere in the codebase!  Please ensure you only call this script from the command line.")