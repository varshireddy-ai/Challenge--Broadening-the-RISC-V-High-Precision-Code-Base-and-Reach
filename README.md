# Tower of Hanoi in Python

This project is a simple implementation of the Tower of Hanoi puzzle in Python.

## Features
- Written in Python 3
- Demonstrates recursion clearly
- Prints every disk move
- Shows the state of all three rods after each move

## How it works
The Tower of Hanoi problem is solved recursively:
1. Move `n-1` disks from source rod to auxiliary rod
2. Move the largest disk from source rod to destination rod
3. Move `n-1` disks from auxiliary rod to destination rod

## Requirements
- Python 3

## Run
```bash
python3 tower_of_hanoi.py
