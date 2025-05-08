from leapYear import isLeapYear

from leapYear import isLeapYear

def validateDate(day, month, year):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            return False
        else:
            return True
    if month == 2:
        if isLeapYear(year):
            if day == 28:
                return True
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    if month == (1, 3, 5, 7, 8, 10, 12) and day > 31:
        return False
    if month == 9 and day > 30:
        return False
    if month == 11 and day > 30:
        return False
    if month == 4 and day > 30:
        return False
    if month == 6 and day > 30:
        return False
    if year < 0:
        return False
    return True

def main():
    day   = int(input("Gib ein Tag ein: "))
    month = int(input("Gib ein Monat ein: "))
    year  = int(input("Gib ein Jahr ein: "))
    print(validateDate(day, month, year))

if __name__ == "main":
    main()
