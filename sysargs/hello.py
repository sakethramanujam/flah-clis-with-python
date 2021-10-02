# !usr/bin/env python3
import sys


def say_hello(name: str, count: int = 5):
    for n in range(count):
        print(f"Hello {name}, Welcome to SunHacks'21!")


def main():
    filename = sys.argv[0]
    name = sys.argv[1]
    count = int(sys.argv[2])
    print(f"Running {filename}...") 
    if not count:
        say_hello(name=name)
    else:
        say_hello(name=name,count=count)


if __name__ == "__main__":
    main()
