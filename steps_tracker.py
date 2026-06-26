# steps_tracker.py

# Daily step counts for one week
steps = [5400, 8200, 12050, 3000, 10500, 7600, 8900]

daily_goal = 10_000

total_steps = 0              # accumulator
hit_goal_at_least_once = False  # boolean flag

for day_steps in steps:
    total_steps += day_steps
    if day_steps >= daily_goal:
        hit_goal_at_least_once = True

average_steps = total_steps / len(steps)

print("Days tracked:", len(steps))
print("Total steps:", total_steps)
print("Average steps per day:", round(average_steps, 2))
print("Hit daily goal at least once?", hit_goal_at_least_once)
