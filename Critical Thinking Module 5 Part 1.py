rainfall_years = int(input("Enter rainfall years: "))
total_months = 0
total_rainfall = 0

for year in range(1, rainfall_years + 1):
    print(f"Year {year}")

    for month in range(1, 13):
        rainfall = float(input(f"Enter inches of rainfall for the month of {month}: "))
        total_rainfall += rainfall
        total_months += 1

    average_rainfall = total_rainfall / total_months

    print(f"\nNumber of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")
