from argparse import ArgumentParser

def abs(x):
    if x > 0:
        return x
    else:
        return -x

def main(x: int):
    abs(x)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("x", type=int)
    args = parser.parse_args()
    main(args.x)
