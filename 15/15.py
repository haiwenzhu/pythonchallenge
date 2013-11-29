#http://www.pythonchallenge.com/pc/return/uzi.html

from datetime import date

first = second = ''
if __name__ == '__main__':
    for year in range(1006, 1997):
        if year % 10 == 6 and date(year, 1, 27).weekday() == 1:
            if (year%4 == 0 and year%100 != 0) or year%400 == 0:
                second = first
                first = year
print(second)
