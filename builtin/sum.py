from argparse import ArgumentParser

def main(iterable):
    print(sum(iterable))

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("item", type=int, nargs="+")
    args = parser.parse_args()
    main(args.item)
