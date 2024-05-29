import time


# Fibonacci function using iteration
import click


def tower_of_hanoi_iterative(n, source, auxiliary, target):
    total_moves = pow(2, n) - 1
    poles = [source, auxiliary, target]

    # If number of disks is even, swap auxiliary and target
    if n % 2 == 0:
        poles[1], poles[2] = poles[2], poles[1]

    # Initialize the poles
    pole_stack = [list(reversed(range(1, n + 1)))] + [[] for _ in range(2)]

    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_disk(pole_stack, poles, 0, 2)
        elif i % 3 == 2:
            move_disk(pole_stack, poles, 0, 1)
        else:  # i % 3 == 0
            move_disk(pole_stack, poles, 1, 2)

def move_disk(pole_stack, poles, from_pole, to_pole):
    from_stack = pole_stack[from_pole]
    to_stack = pole_stack[to_pole]

    if len(from_stack) > 0 and (len(to_stack) == 0 or to_stack[-1] > from_stack[-1]):
        disk = from_stack.pop()
        to_stack.append(disk)
        print(f"Move disk {disk} from {poles[from_pole]} to {poles[to_pole]}")
    else:
        disk = to_stack.pop()
        from_stack.append(disk)
        print(f"Move disk {disk} from {poles[to_pole]} to {poles[from_pole]}")

# Call the function
tower_of_hanoi_iterative(3, 'A', 'B', 'C')


# Fibonacci function using recursion
def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, target, source)

@click.command()
@click.option('--mode', type=click.Choice(['rec', 'ite']), default='rec')
@click.option('--n', default=10)
def main(mode: str, n: int):
    hanoi_functions = {
        'rec': tower_of_hanoi,
        'ite': tower_of_hanoi_iterative
    }

    result = hanoi_functions.get(mode)(8, 'A', 'B', 'C')

    print(result)


if __name__ == "__main__":
    main()


