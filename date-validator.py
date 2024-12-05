#Adrián Díaz Azofeifa

#Check if tuple is a valid date
def is_date_valid(tuple_date):
    try:
        year, month, day = map(int, tuple_date)
        return check_date((year, month, day))
    except:
        return False


def check_date(tuple_date):
    year, month, day = tuple_date
    is_leap = check_leap(year)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 2:
        if is_leap and day == 29:
            return True
        elif 1 <= day <= 28:
            return True
        else:
            return False
    else:
        return False


#Check if year is a leap year
def is_leap_year(num):
    try:
        if isinstance(num, int):
            if num > 1582: # isinstance(num, int)
                # isLeap = check_leap(num)
                return check_leap(num)
            else:
                return False
        else:
            raise Exception()
    except:
        return 'Please enter a number.'


def check_leap(num):
    not_gregorian = num < 1582
    if num % 100 == 0:
        if num % 400 == 0:
            return True
        else:
            return False or not_gregorian
    elif num % 4 == 0:
        return True
    else:
        return False


#Check if date is a valid Gregorian date
def is_gregorian_date(tuple_date):
    try:
        if is_date_valid(tuple_date):
            if check_gregorian(tuple_date):
                return True
            else:
                return False
        else:
            return False
    except:
        return False


def check_gregorian(tuple_date):
    year, month, day = tuple_date
    if year < 1582:
        return False
    elif year == 1582:
        if month < 10:
            return False
        elif month == 10 and 1 <= day < 15:
            return False
        elif month == 10 and 15 <= day <= 31:
            return True
        else:
            return True
    elif year > 1582:
        return check_date(tuple_date)


#Returns the date of the day after
def next_day(tuple_date):
    try:
        if check_gregorian(tuple_date):
            year, month, day = tuple_date
            new_year = year
            new_month = month
            new_day = day
            is_leap = check_leap(year)
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
                if day == 31:
                    new_day = 1
                    new_month = month + 1
                else:
                    new_day = day + 1
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day == 30:
                    new_day = 1
                    new_month = month + 1
                else:
                    new_day = day + 1
            elif month == 2:
                if day == 28 and is_leap:
                    new_day = 29
                elif day == 28 and not is_leap:
                    new_day = 1
                    new_month = 3
                elif day == 29 and is_leap:
                    new_day = 1
                    new_month = 3
                else:
                    new_day = day + 1
            elif month == 12:
                if day == 31:
                    new_day = 1
                    new_month = 1
                    new_year = year + 1
                else:
                    new_day = day + 1
            result = (new_year, new_month, new_day)
            return result
        else:
            raise Exception()
    except:
        return 'Please input a valid date.'


#Returns how many days have passed since January 1st of the same year
def days_since_jan1st(tuple_date):
    try:
        year, month, day = map(int, tuple_date)
        if check_gregorian(tuple_date):
            days_count: int = 0
            days_jan: int = 30
            days_feb: int = 58
            days_march: int = 89
            days_april: int = 119
            days_may: int = 150
            days_june: int = 180
            days_july: int = 211
            days_aug: int = 242
            days_sept: int = 272
            days_oct: int = 303
            days_nov: int = 333
            leap_counts = month > 2
            if month == 1 and day == 1:
                return days_count
            elif month == 1 and 1 < day:
                days_count = day - 1
            elif month == 2:
                days_count = day + days_jan
            elif month == 3:
                days_count = day + days_feb
            elif month == 4:
                days_count = day + days_march
            elif month == 5:
                days_count = day + days_april
            elif month == 6:
                days_count = day + days_may
            elif month == 7:
                days_count = day + days_june
            elif month == 8:
                days_count = day + days_july
            elif month == 9:
                days_count = day + days_aug
            elif month == 10:
                days_count = day + days_sept
            elif month == 11:
                days_count = day + days_oct
            elif month == 12:
                days_count = day + days_nov
            else:
                raise Exception()

            if check_leap(year) and leap_counts:
                return days_count + 1
            else:
                return days_count
        else:
            raise Exception()
    except:
        return 'Please input a valid date.'


#Returns the day of the week of January 1st of that year
#Returns numbers 0 through 6. 0 is Sunday, 6 is Saturday
def jan1st_day(year):
    try:
        if isinstance(year, int):
            if year > 1582:
                return count_days(year)
            else:
                return 'Please input a Gregorian year.'
        else:
            raise Exception()
    except:
        return 'Please input a valid year.'


def count_days(year):
    counter = 6
    start = 1583
    while start < year:
        if check_leap(start):
            counter = counter + 2
        else:
            counter = counter + 1
        start = start + 1
    return counter % 7
