from datetime import datetime
import sys
"""
Input: birth date (YYYY-MM-DD format)
Output: days old and weeks old
"""


def main():
    num_days_old = days_old( input("Enter birth date in YYYY-MM-DD format: "),  datetime.now() )
    num_weeks_old = days_to_weeks(num_days_old)
    print( str(num_days_old) + " Days Old")
    print( str(num_weeks_old) + " Weeks Old")

# computes the difference of the current date (today) and the date entered by the user
def compute_days_difference(init_date, today):
    diff = today - init_date
    diff = str(diff)
    print("diff="+diff)
    days_diff, junk = diff.split(',')  # remove the time portion, only need the days
    return days_diff

# takes as input an integer number of days and converts it into an integer number of weeks
def days_to_weeks(days):
    weeks = int( int(days)//7 ) # Note: using // for integer division, don't want a decimal
    return weeks

# creates a date object from the date input by the user
def my_create_date(d):
    # make sure the date is in the specified YYYY-MM-DD format
    try:
        year,month,day = d.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        sys.exit("Invalid date format")
    d = datetime(year, month, day)
    return d

# returns the number of days old
def days_old(init_date, today):
    init_date = my_create_date(init_date)
    num_days_old = compute_days_difference(init_date, today)
    num_days_old, junk = num_days_old.split(' ') # remove the text "days" or "day" after the integer number of days
    return num_days_old


if __name__ == "__main__":
    main()
