# date-validator-python
Little program to validate dates according to the Gregorian calendar in Python.
Made using Python 3.8.10.

The program has 5 main functions and 5 auxiliary functions to:

- Check if the date input is valid and in correct format.
- Check if input year is a leap year, according to the Gregorian calendar's restrictions.
- Given a valid date, return the following day's date.
- Given a valid date, return how many days has it been since January 1st.
- Return the day of the week of January 1st of a given year as an integer from 0 through 6: 0 is Sunday, 6 is Saturday.

It uses a tuple in the format (year, month, day).

Use examples:
- is_date_valid((1999,12,12)) returns True
- is_date_valid((1999,12,35)) returns False
- is_leap_year((1996)) returns True
- is_leap_year((1999)) returns False
- is_gregorian_date((1582,1,1)) returns False
- is_gregorian_date((1583,1,1)) returns True
- next_day((2000,2,29)) returns (2000,3,1)
- next_day((1999,12,31)) returns (2000,1,1)
- next_day((2000,2,30)) returns instruction message
- days_since_jan1st((1992,2,29) returns 59
- days_since_jan1st((2000,1,1) returns 0
- days_since_jan1st((1992,2,30) returns instruction message
- jan1st_day(2025) returns 3.

Quick introduction to the Gregorian calendar:

It went into effect in October 1582 by the Pope's instructions. Fixes mistakes in time keeping introduced by the previous calendar, the Julian calendar. Corrects the definition of a leap year, now it's not only a year divisible by 4, but also by 400. Therefore the year 1600 and 2000 are leap years but 1700 and 1900 aren't. And lastly Thursday, October 4th, 1582 was followed by Friday, October 15th.

