import time


# Fibonacci function using iteration
import click


def fibonacci_iterative(n):
    start_time = time.time()
    if n <= 2:
        return 1 if n else 0
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
    end_time = time.time()
    print(f"Time taken by iterative function: {end_time - start_time} seconds")
    return b



# Fibonacci function using recursion
def fibonacci_recursive(n):
    start_time = time.time()
    if n <= 2:
        return 1 if n else 0
    else:
        result = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    end_time = time.time()
    print(f"Time taken by recursive function: {end_time - start_time} seconds")
    return result


@click.command()
@click.option('--mode', type=click.Choice(['rec', 'ite']), default='ite')
@click.option('--n', default=10)
def main(mode: str, n: int):
    fibonacci_functions = {
        'rec': fibonacci_recursive,
        'ite': fibontacci_iterative
    }

    result = fibonacci_functions.get(mode)(n)

    print(result)


if __name__ == "__main__":
    main()


