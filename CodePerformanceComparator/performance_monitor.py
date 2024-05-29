import importlib
import time
import memory_profiler
import click
import psutil

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
    start_cpu = psutil.cpu_percent(interval=None)

    end_time = time.time()
    end_mem = memory_profiler.memory_usage()[0]
    end_cpu = psutil.cpu_percent(interval=None)

    return end_time - start_time, end_mem - start_mem, end_cpu - start_cpu


@click.command()
@click.option('--builtin_name', default='abs')
@click.option('--n', default=10)
def main(builtin_name: str, n: int):

    original_builtin = getattr(builtin, builtin_name)
    test_builtin = getattr(manual_builtin, builtin_name)
    results_original = {
        'RAM': [],
        'CPU': [],
        'time': [],
    }
    results_test = {
        'RAM': [],
        'CPU': [],
        'time': [],
    }

    for i in range(n):
        time_original, ram_original, cpu_original = measure_performance(original_builtin, **builtin_args[builtin_name])
        time_test, ram_test, cpu_test = measure_performance(test_builtin, **builtin_args[builtin_name])

        results_original['RAM'].append(ram_original)
        results_test['RAM'].append(ram_test)
        results_original['CPU'].append(cpu_original)
        results_test['CPU'].append(cpu_test)
        results_original['time'].append(time_original)
        results_test['time'].append(time_test)




if __name__ == '__main__':
    main()
