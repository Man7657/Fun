# Function to check whether given year is leap year or not

y = int(input("Enter your choice of the year : "))


def leap_or_not(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Its a Leap Year")
            else:
                print("Its a not Leap Year")
        else:
            print("Its a Leap Year")
    else:
        print("Its not a Leap Year")


leap_or_not(y)
