#checks if the year provided is a leap year. as the dates will differ if it is
def is_leap_year():
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

date = input("Please enter the date in this format: eg:20 December 2004\n")

#splits the entered date into day, month and year respectively. 
day, month, year = date.split()

day = int(day)
month = month.lower()
year = int(year)

def main():
    #add the last two digits to a quarter of the 
    step_1 = year % 100 * 1/4

    #Add to that the day of the month and the Month Key number for that month:

    #if month is jan, the key is 0 for leap year and 1 for non-leap year
    if month == "january":
        if is_leap_year():
            month_key = 0
        else:
            month_key = 1

    #if the month is feb, the key is 3 for leap year and 4 for non-leap year
    elif month == "february":
        if is_leap_year():
            month_key = 3
        else:
            month_key = 4

    #if the month is march, key is 4
    elif month == "march":
        month_key = 4

    #if the month is april, key is 0
    elif month == "april":
        month_key = 0

    #if the month is may, key is 2
    elif month == "may":
        month_key = 2

    elif month == "june":
        month_key = 5

    elif month == "july":
        month_key = 0

    elif month == "august":
        month_key = 3

    elif month == "september": 
        month_key = 6

    elif month == "october":
        month_key = 1

    elif month == "november":
        month_key = 4

    elif month == "december":
        month_key = 6

    #if it is none of the above, there is a spelling mistake and the program ends
    else:
        print("Please check if you have entered correct spelling.")
        exit()
    
    #if the year is between 2000 and 2099, subtract 1 from the sum.
    if 2000 < year < 2099:
        step_2 = int(step_1) + day + month_key + int(year % 100) - 1
    else:
        step_2 = int(step_1) + day + month_key + int(year % 100)

    #Divide the sum by 7. The remainder is the day of the week! One is Sunday, two is sMonday, and so on. If there is no remainder, the day is Saturday. 
    step_3 = step_2 % 7

    print(f"The day of the week is : {days[step_3 - 1]}")

main()