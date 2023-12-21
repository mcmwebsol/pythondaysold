# pythondaysold
The program will output the number of days and weeks old when the birth date is input at the prompt.  The main code for the project is in the file project.py

The program expects the birth date to be in the YYYY-MM-DD format, that is, a four digit year, followed by a single dash, then followed by the month as two digits, using a leading zero if the month is less than ten, then another dash, and finally the day of the month as two digits, much like the month itself.  Invalid date entry will cause the program to exit with the error message "Invalid date format".  A try block is used to catch any value error in the birth date input.

The project is written in the programming language Python and uses a total of two libraries: sys and datetime.
The sys library is used only for the sys.exit() call if the birth date is entered in an invalid format.
The datetime library is used for computing the difference between the birth date and today's date.

The program has four custom functions:
 compute_days_difference(init_date, today)
   This function computes the difference between the current date, passed in the parameter "today", and the date entered by the user, which
    is in the parameter "init_date".

 days_to_weeks(days)
   This function takes as input an integer number of days in the parameter "days" and converts it into an integer number of weeks and returns that value.

 my_create_date(d)
   This function creates a date object from the date input by the user.  The date is passed in via the parameter "d".

 days_old(init_date, today)
   This function returns the number of days old.  It takes two parameters as input: "init_date", which is the birth date, and "today" which is the current date.

The tests are in the file test_project.py

Usage: Please enter the birth date in the YYYY-MM-DD format when prompted
