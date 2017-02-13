
import argparse


parser = argparse.ArgumentParser(description="Add a series of integers to eachother")
parser.add_argument('a', help='Number 1', type=int)
parser.add_argument('b', help='Number 2', type=int)
# parser.add_argument('--number', '-n', action='append', default=[], type=int, help='A number to add!')


def main(args):
    print(args)
    numbers = [args.a, args.b]
    print('The sum is:', sum(numbers))


if __name__ == '__main__':
    main(parser.parse_args())

