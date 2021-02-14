input_year = input("Please enter a year to see if it is a Leap Year: ")  
while input_year.isdigit() == False or int(input_year) == 0 :
    input_year = input("It is an invalid entry. Please input a positive integer number:  ")
if int(input_year) %4 == 0 and int(input_year)%400 == 0  :
    print(f"{int(input_year)} is a leap year ")
elif int(input_year) %4 == 0 and int(input_year)%100 == 0 and int(input_year)%400 != 0: 
    print(f"{int(input_year)} is not a leap year ")
else:
    print(f"{int(input_year)} is not a leap year ")

