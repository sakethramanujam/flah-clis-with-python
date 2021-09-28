# !usr/bin/env python3
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Say Hello to somebody  with command line!")
    parser.add_argument('-n', '--name',
                        type=str, help="Type a name", required=True)
    parser.add_argument('-c', '--count', type=int,
                        help="Number of Times you want to wish them")
    args = parser.parse_args()
    return args


def say_hello(name: str, count: int = 5):
    for n in range(count):
        print(f"Hello {name}, Welcome to SunHacks'21!")


def main():
    arguments = get_args()
    name, count = arguments.name, arguments.count
    if count:
        say_hello(name=name, count=count)
    else:
        say_hello(name=name)


if __name__ == "__main__":
    main()
