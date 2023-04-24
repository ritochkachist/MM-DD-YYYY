# Margarita Chistiakova
# 10/24/2022
# Additional project 9

print("Please enter the date in the following format MM/DD/YYYY")
date = input()

month = date[0:2]
print(f"The month read from the date is {month}.")
day = date[3:5]
print(f"The day read from the date is {day}.")
year = date[6:11]
print(f"The year read from the date is {year}.")

if month == "01":
  print(f"{day} January, {year}")
elif month == "02":
  print(f" {day} February, {year}")
elif month == "03":
  print(f" {day} March, {year}")
elif month == "04":
  print(f" {day} April, {year}")
elif month == "05":
  print(f" {day} May, {year}")
elif month == "06":
  print(f" {day} June, {year}")
elif month == "07":
  print(f" {day} July, {year}")
elif month == "08":
  print(f" {day} August, {year}")
elif month == "09":
  print(f" {day} September, {year}")
elif month == "10":
  print(f" {day} October, {year}")
elif month == "11":
  print(f" {day} November, {year}")
elif month == "12":
  print(f" {day} December, {year}")