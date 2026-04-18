# tower_of_hanoi.py
# Challenge 1: Tower of Hanoi
# This program demonstrates recursion by solving the Tower of Hanoi puzzle.
# It prints each move and shows the current state of the three rods.

import time

move_count = 0


def print_rods(rods):
    """Print the current state of all rods."""
    print("\nCurrent Rod State:")
    for rod_name in ["A", "B", "C"]:
        print(f"{rod_name}: {rods[rod_name]}")
    print("-" * 30)


def move_disk(from_rod, to_rod, rods):
    """Move the top disk from one rod to another and print the updated state."""
    global move_count
    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    move_count += 1
    print(f"Move {move_count}: disk {disk} from {from_rod} to {to_rod}")
    print_rods(rods)
    time.sleep(0.3)


def solve_hanoi(n, source, auxiliary, destination, rods):
    """
    Recursive function to solve Tower of Hanoi.

    Steps:
    1. Move n-1 disks from source to auxiliary
    2. Move the largest disk from source to destination
    3. Move n-1 disks from auxiliary to destination
    """
    if n == 1:
        move_disk(source, destination, rods)
        return

    solve_hanoi(n - 1, source, destination, auxiliary, rods)
    move_disk(source, destination, rods)
    solve_hanoi(n - 1, auxiliary, source, destination, rods)


def main():
    print("Tower of Hanoi Demonstration")
    print("----------------------------")

    try:
        n = int(input("Enter number of disks: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    rods = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": []
    }

    print("\nInitial State:")
    print_rods(rods)

    solve_hanoi(n, "A", "B", "C", rods)

    print("\nPuzzle solved!")
    print(f"Total moves required: {move_count}")
    print(f"Expected minimum moves: {2**n - 1}")


if __name__ == "__main__":
    main()
