from datetime import datetime, timedelta 

# Define the current date 

days_ago = input("how many days ago would you like to check?: ")
days_ago = int(days_ago)
current_date = datetime.now()

# Subtract days 
previous_date = current_date - timedelta(days= days_ago)

# Get the day of the week for the previous date 

previous_day_of_week = previous_date.strftime("%A")
print(f"The date {days_ago} days ago was {previous_date.date()}, and it was a {previous_day_of_week}.")

