# Write a Python program to check if a given year is a leap year.
year = int(input("Enter the year:"))
if year % 4 ==0 and year % 100 !=0 or year % 400 == 0:
    print("year is leap year")
else:
    print("year is not leap year")