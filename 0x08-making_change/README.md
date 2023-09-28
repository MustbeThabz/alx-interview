king Change

A Python function to find the fewest number of coins needed to reach a given total amount using dynamic programming.

## Problem Statement

Given a list of coin values and a target total, this function calculates the minimum number of coins required to reach the total, following these rules:

- If the total is 0 or less, it returns 0.
- If it's impossible to reach the total with the given coins, it returns -1.
- You can assume you have an infinite number of each coin denomination.

## Usage

### Prerequisites

- Python 3.7 or higher


### Function Description

The `makeChange` function takes two parameters:

- `coins`: A list of coin values (denominations) you possess.
- `total`: The target total to reach.

It returns the minimum number of coins needed or -1 if not possible.

### Example Usage

```python
from making_change import makeChange

# Example 1
coins = [1, 2, 25]
total = 37
result = makeChange(coins, total)
print(result)  # Output: 7

# Example 2
coins = [1256, 54, 48, 16, 102]
total = 1453
result = makeChange(coins, total)
print(result)  # Output: -1

