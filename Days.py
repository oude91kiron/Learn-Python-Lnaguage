

def leapYear(year):
    if year % 4 == 0 :
        return True
        if year % 100 == 0 :
            return False
            if year % 400 == 0:
                return True
    return False


def daysInMon(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
       or month == 8 or month == 10 or month == 12:
         return 31
    else:
        if month == 2 :
            if leapYear(year) :
                return 29
            else:
                return 28
        else :
           return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMon(year, month) and day > 0 :
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
    

# helper function
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2 :
               return True
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    while month1 < 13 and month2 < 13 and day1 < 32 and day2 < 32:
         assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
         days = 1
         while dateIsBefore(year1, month1, day1, year2, month2, day2):
             year1, month1, day1 = nextDay(year1, month1, day1)
             days += 1
         return days
    print "month must be less than 13 and day less than 32"

print "Test"
print "2012 leapYear"
print "The number of days between two dates", daysBetweenDates(2011, 4, 22, 2012, 4, 22)
print " "
print "The number of days that Mr.Room lived until now", daysBetweenDates(1991, 10, 23, 2018, 3, 9)
print " "
print "The number of days that Ms.Green lived until now", daysBetweenDates(1972, 12, 10, 2018, 3, 9) 
print " "
print "The number of days that Mr.White lived until now", daysBetweenDates(1961, 9 , 9, 2018, 3, 9)
