year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

def judgeMonth(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
 
 
def countDays(year, month, day):
    isRun = judgeMonth(year)
    if(isRun):
        monthDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        monthDay = [31, 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sumDay = sum(monthDay[:(month - 1)]) + day
    return sumDay
 

ans = countDays(year, month, day)
print(ans)
