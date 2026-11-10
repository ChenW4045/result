exercise_minutes = [20, 0, 35, 15, 40]
total_minutes = 0
active_days = 0
target_days = 0

for e in exercise_minutes:
    total_minutes += e 
    if e > 0:
        active_days += 1
    if e >= 30:
        target_days += 1
print('總時長:',total_minutes)
print('運動天數:',active_days)
print('達標天數:',target_days)
