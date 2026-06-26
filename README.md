# Fitness Steps Tracker

A simple Python script that tracks daily step counts for a week and reports:

- Total steps
- Average steps per day
- Whether the daily goal was hit at least once

## How it works

The script:

- Stores daily step counts in a list
- Uses a **running total** (accumulator) to sum all steps
- Uses a **boolean flag** to check if any day hit the goal
- Prints a short summary at the end

## Example

Given this data:

```python
steps = [5400, 8200, 12050, 3000, 10500, 7600, 8900]
daily_goal = 10_000
