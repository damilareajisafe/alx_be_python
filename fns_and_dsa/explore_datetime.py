# from datetime
import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date():
    num_of_days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.date.today()
    future_date = today + datetime.timedelta(days=num_of_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}")



# display_current_datetime()
# calculate_future_date()
