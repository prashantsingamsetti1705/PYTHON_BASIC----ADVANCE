#InnerLoopsEx7.py
import calendar
for year in range(2023,2025): # Outer Loop Supply the Value to Inner
    print("-"*50)
    print("YEAR :{}".format(year))
    print("-" * 50)
    for mon in range(1,13): # Inner Loop--generates the Table
         print("\t{}".format(calendar.month(year,mon)))
    else:
        print("-" * 50)
else:
    print("-" * 50)