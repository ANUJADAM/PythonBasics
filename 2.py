y=int(input("Enter a year"))
year="leap year" if y % 400==0 else "leap year" if y % 4==0 and y % 100 !=0 else "Not a leap year" 
print(year)