import pandas as pd

def generate_schedule(staff, shifts):
    schedule = {}
    for i, shift in enumerate(shifts):
        schedule[shift] = staff[i % len(staff)]
    return schedule

staff = ["Alex", "Jordan", "Taylor", "Sam"]
shifts = ["Mon AM", "Mon PM", "Tue AM", "Tue PM"]

print(generate_schedule(staff, shifts))
