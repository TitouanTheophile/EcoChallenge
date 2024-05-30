from argparse import ArgumentParser

def predicate(item):
    return item % 3 == 0

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        [i for i in iterable if predicate(i)]

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
