# 3233 sols = 3321 days, 21 hours, 6 minutes and 3 seconds.
#  A sol is 24 hours, 39 minutes and 35.244 seconds.

# 24h (mars) = 24.65979h (earth)

solLength = 24.65979

sols = int(input())  # Get the amount of sols passed.
hoursTotal = sols * solLength  # Earth hours in the amount of sols.

days = int(hoursTotal / 24)
hours = hoursTotal - days * 24
minutes = (hours - int(hours)) * 60
seconds = (minutes - int(minutes)) * 60

print(f"{sols} sols = {days} days, {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds")
