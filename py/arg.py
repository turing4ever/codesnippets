import argparse

def main():
    # create the top-level parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help')
    
    # create the parser for the "a" command
    parser_a = subparsers.add_parser('a', help='a help')
    parser_a.add_argument('--bar', type=int, help='bar help')
    
    # create the parser for the "b" command
    parser_b = subparsers.add_parser('b', help='b help')
    parser_b.add_argument('--baz', choices='XYZ', help='baz help')

    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
