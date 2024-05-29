import importlib
import time
import memory_profiler
import click

import builtin
import manual_builtin


builtin_args = {
    "abs": {

    },
    "aiter": {

    },
    "all": {

    },
    "anext": {

    },
    "any": {

    },
    "ascii": {

    },
    "bin": {

    },
    "bool": {

    },
    "breakpoint": {

    },
    "bytearray": {

    },
    "bytes": {

    },
    "callable": {

    },
    "chr": {

    },
    "classmethod": {

    },
    "compile": {

    },
    "complex": {

    },
    "delattr": {

    },
    "dict": {

    },
    "dir": {

    },
    "divmod": {

    },
    "enumerate": {

    },
    "eval": {

    },
    "exec": {

    },
    "filter": {

    },
    "float": {

    },
    "format": {

    },
    "frozenset": {

    },
    "getattr": {

    },
    "globals": {

    },
    "hasattr": {

    },
    "hash": {

    },
    "help": {

    },
    "hex": {

    },
    "id": {

    },
    "input": {

    },
    "int": {

    },
    "isinstance": {

    },
    "issubclass": {

    },
    "iter": {

    },
    "len": {

    },
    "list": {

    },
    "locals": {

    },
    "map": {

    },
    "max": {

    },
    "memoryview": {

    },
    "min": {

    },
    "next": {

    },
    "object": {

    },
    "oct": {

    },
    "open": {

    },
    "ord": {

    },
    "pow": {

    },
    "print": {

    },
    "property": {

    },
    "range": {

    },
    "repr": {

    },
    "reversed": {

    },
    "round": {

    },
    "set": {

    },
    "setattr": {

    },
    "slice": {

    },
    "sorted": {

    },
    "staticmethod": {

    },
    "str": {

    },
    "sum": {

    },
    "super": {

    },
    "tuple": {

    },
    "type": {

    },
    "vars": {

    },
    "zip": {

    },
    "__import__": {

    }
}


def measure_performance(func, **args):
    start_time = time.time()
    start_mem = memory_profiler.memory_usage()[0]

    result = func(**args)

    end_time = time.time()
    end_mem = memory_profiler.memory_usage()[0]

    return result, end_time - start_time, end_mem - start_mem


@click.command()
@click.option('--builtin_name', type=click.Choice(['fibonacci', 'hanoi']), default='algorithm1')
def main(builtin_name: str):
    original_builtin = getattr(builtin, builtin_name)
    manual_builtin = getattr(manual_builtin, builtin_name)

    _, time_good, mem_good = measure_performance(original_builtin, **builtin_args[builtin_name])
    _, time_wrong, mem_wrong = measure_performance(manual_builtin, **builtin_args[builtin_name])

    print(f"Good Practice - Time: {time_good} seconds, Memory: {mem_good} MiB")
    print(f"Wrong Practice - Time: {time_wrong} seconds, Memory: {mem_wrong} MiB")


if __name__ == '__main__':
    main()
