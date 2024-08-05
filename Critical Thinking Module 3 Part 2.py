start_time = int(input("Enter the current hour: "))
alarm_time = int(input("Enter the number of hours the alarm should go off in: "))
total_time = int(start_time + alarm_time)
days = int(total_time / 24)
time_after_days = total_time - (days * 24)

if days < 1:
    print(f"The alarm will go off at {total_time:02d}:00")
else:
    print(f"The alarm will go off at {time_after_days:02d}:00")
