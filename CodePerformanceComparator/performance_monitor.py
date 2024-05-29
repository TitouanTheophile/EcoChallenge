import importlib
import time
import memory_profiler
import click
import psutil
import json

import builtin
import manual_builtin

from config import builtin_args

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

    for i in range(n):
        time_original, ram_original, cpu_original = measure_performance(original_builtin, **builtin_args[builtin_name])
        time_test, ram_test, cpu_test = measure_performance(test_builtin, **builtin_args[builtin_name])

        results['Original']['RAM'].append(ram_original)
        results['Test']['RAM'].append(ram_test)
        results['Original']['CPU'].append(cpu_original)
        results['Test']['CPU'].append(cpu_test)
        results['Original']['time'].append(time_original)
        results['Test']['time'].append(time_test)

    with open('report.json', 'w') as file:
        json.dump(results, file)


if __name__ == '__main__':
    main()
