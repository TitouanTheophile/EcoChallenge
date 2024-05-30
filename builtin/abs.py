import builtins
from argparse import ArgumentParser


def main(x: int):
    # To uncomment when in prod
    # builtins.abs(x)

    # For testing
    print(builtins.abs(x))

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("x", type=int)
    args = parser.parse_args()
    main(args.x)
