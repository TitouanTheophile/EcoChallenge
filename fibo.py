# Fibonacci function using iteration
import click


def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


# Fibonacci function using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


@click.command()
@click.option('--mode', type=click.Choice(['rec', 'ite']), default='ite')
@click.option('--n', default=10)
def main(mode: str, n: int):
    fibonacci_functions = {
        'rec': fibonacci_recursive,
        'ite': fibonacci_iterative
    }

    result = fibonacci_functions.get(mode)(n)

    print(result)


if __name__ == "__main__":
    main()
