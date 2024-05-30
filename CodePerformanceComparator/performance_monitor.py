import importlib
import time
from memory_profiler import memory_usage
import click
import psutil
import json

import builtin
import manual_builtin

from config import builtin_args


def measure_performance(func, **args):
    mem_usage = memory_usage((func, args.values()), interval=.001)

    return mem_usage


@click.command()
@click.option('--builtin_name', default='abs')
@click.option('--n', default=10)
def main(builtin_name: str, n: int):

    original_builtin = getattr(builtin, builtin_name)
    test_builtin = getattr(manual_builtin, builtin_name)
    results = {
        'Original': {
            'RAM': [],
            'CPU': [],
            'time': [],
        },
        'Test': {
            'RAM': [],
            'CPU': [],
            'time': [],
        }
    }

    test_res = measure_performance(test_builtin, **builtin_args[builtin_name])
    #results['Test']['RAM'].append(res)

    origin_res = measure_performance(original_builtin, **builtin_args[builtin_name])
    #results['Original']['RAM'].append(res)

    print(f'Original: {origin_res}\n'
          f'Test: {test_res}')


if __name__ == '__main__':
    main()
