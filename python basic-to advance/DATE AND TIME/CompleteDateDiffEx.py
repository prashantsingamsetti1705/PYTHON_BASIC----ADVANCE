#Complete DateTime Difference interms of Year, months, days, hours , minutes and second...etc
#CompleteDateDiffEx.py
from datetime import datetime
from dateutil.relativedelta import relativedelta

start_time = datetime(2022, 4, 28, 12, 0, 0)
end_time = datetime(2024, 4, 28, 12, 0, 0)

# Calculate the difference
time_diff = relativedelta(end_time, start_time)

# Display the result
print("Years:", time_diff.years)      # Output: Years: 1
print("Months:", time_diff.months)    # Output: Months: 5
print("Days:", time_diff.days)        # Output: Days: 2
print("Hours:", time_diff.hours)      # Output: Hours: 20
print("Minutes:", time_diff.minutes)  # Output: Minutes: 15
print("Seconds:", time_diff.seconds)  # Output: Seconds: 25