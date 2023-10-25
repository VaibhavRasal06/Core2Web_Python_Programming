month = input("Enter a month to get its number of days: ")

if (month == "January" or month == "March" or month == "May" or month == "July" or month == "September" or month == "December"):
    print("{} is a 31-day month".format(month))

elif (month == "February"):
    print("{} is a 28/29-day month".format(month))

else:
    print("{} is a 30-day month".format(month))
