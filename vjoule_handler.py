import os
import sys

vjoule_cmd = "vjoule"
python_cmd = "python"


def parse_results(input: str) -> dict:
    pass


def eval_command(cmd: str, *args) -> dict:
    args_as_str = " ".join(args)
    stream = os.popen(f"{vjoule_cmd} {cmd} {args_as_str}")
    return parse_results(stream.read())


def eval_python(filepath: str, *args):
    args_as_str = " ".join(args)
    eval_command(f"{python_cmd} {filepath} {args_as_str}")


def main() -> int:
    #eval_python('my_python.py', 'param') 
    return 0


if __name__ == '__main__':
    sys.exit(main())

