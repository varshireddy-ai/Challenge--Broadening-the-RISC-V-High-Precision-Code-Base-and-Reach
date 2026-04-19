# tower_of_hanoi.py
# Challenge 1: Tower of Hanoi
# This program demonstrates recursion by solving the Tower of Hanoi puzzle.
# It also shows simple console-based graphics for visualization.

import time

move_count = 0


def print_rods(rods, total_disks):
    """
    This function prints the rods using simple graphics.

    👉 ITERATION:
    - Uses loops to display rod levels visually.
    - Outer loop: iterates over levels (top to bottom)
    - Inner loop: iterates over rods (A, B, C)
    """
    print()

    for level in range(total_disks - 1, -1, -1):   # Iteration over levels
        for rod in ["A", "B", "C"]:                # Iteration over rods
            if level < len(rods[rod]):
                disk = rods[rod][level]
                print(f"{disk}".center(8), end="")
            else:
                print("|".center(8), end="")
        print()

    print("   A       B       C")
    print("-" * 30)


def move_disk(from_rod, to_rod, rods, total_disks):
    """
    Moves a disk from one rod to another.

    👉 ITERATION EFFECT:
    - Called repeatedly during recursion
    - Updates rod state step-by-step
    """
    global move_count

    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    move_count += 1

    print(f"Move {move_count}: disk {disk} from {from_rod} to {to_rod}")
    print_rods(rods, total_disks)
    time.sleep(0.3)


def solve_hanoi(n, source, auxiliary, destination, rods, total_disks):
    """
    👉 CORE RECURSION FUNCTION

    This function demonstrates RECURSION.

    Recursion works by breaking the problem into smaller subproblems.

    Steps:
    1. Move (n-1) disks from source → auxiliary  (recursive call)
    2. Move the largest disk to destination       (actual move)
    3. Move (n-1) disks from auxiliary → destination (recursive call)

    👉 BASE CASE:
    When n == 1 → directly move the disk (no further recursion)

    👉 RECURSIVE CASE:
    Function calls itself with smaller values of n
    """

    # BASE CASE (stops recursion)
    if n == 1:
        move_disk(source, destination, rods, total_disks)
        return

    # RECURSIVE STEP 1
    solve_hanoi(n - 1, source, destination, auxiliary, rods, total_disks)

    # MOVE CURRENT DISK
    move_disk(source, destination, rods, total_disks)

    # RECURSIVE STEP 2
    solve_hanoi(n - 1, auxiliary, source, destination, rods, total_disks)


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

    # 👉 ITERATION USED IN VISUAL DISPLAY
    print_rods(rods, n)

    # 👉 RECURSION STARTS HERE
    solve_hanoi(n, "A", "B", "C", rods, n)

    print("\nPuzzle solved!")
    print(f"Total moves required: {move_count}")
    print(f"Expected minimum moves: {2**n - 1}")


if __name__ == "__main__":
    main()
