import argparse

def tt():
    """try out the code in tutorial"""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='cmd')
    parser_echo = subparsers.add_parser('echo', help='echo help')
    parser_echo.add_argument("echo")
    parser_square = subparsers.add_parser('square', help="display a square of a given number")
    parser_square.add_argument("square", help="Calculate the square", type=float)
    parser_square.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
    args = parser.parse_args()
    if args.cmd and args.cmd=='echo':
        print(args.echo)
    if args.cmd and args.cmd=='square':
        answer = args.square**2
        if args.verbose:
            print("the square of {} equals {}".format(args.square, answer))
        else:
            print(answer)

if __name__ == '__main__':
    tt()
