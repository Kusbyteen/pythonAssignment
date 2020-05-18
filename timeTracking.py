import time
import datetime
import csv
from tkinter import messagebox

print("Note: Date and Time is in UTC")
#messagebox.showinfo(title="Time Notice", message="Time and Date are in UTC")
with open('file.csv', 'a') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    start_datetime =  input("Please Enter Start Date and Time (dd/mm/yyyy and h:m:s): ")
    start_datetime_stamp = datetime.datetime.strptime(start_datetime, "%d/%m/%Y %H:%M:%S")
    end_datetime =  input("Please Enter End Date and Time (dd/mm/yyyy and h:m:s): ")
    end_datetime_stamp = datetime.datetime.strptime(end_datetime, "%d/%m/%Y %H:%M:%S")
    datetime_diff = end_datetime_stamp - start_datetime_stamp
    if end_datetime_stamp > start_datetime_stamp:
        hours_difference = abs(datetime_diff).total_seconds() / 3600.0
        salary =  hours_difference * 5
        salary_in_dollars = (str(salary) + " dollars")
        print(salary_in_dollars)
        w.writerow(["START TIME AND DATE", "END TIME AND DATE", "SALARY IN DOLLARS"])
        w.writerow([start_datetime_stamp, end_datetime_stamp, salary_in_dollars])
    else:
        print("Check your input Again")
