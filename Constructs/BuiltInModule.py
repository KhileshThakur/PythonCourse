# #math
# import math as mt
# print(mt.sqrt(16))
# print(mt.pi)


# #random 
# import random as rd
# print(rd.randint(1, 10))
# items=['a','b','c','c']
# # print(rd.choice(items))
# # print(rd.shuffle(items))
# print(items)

# #os module
# import os 
# print(os.name)
# print(os.path)
# print(os.getcwd())
# # print(os.mkdir('newdir'))
# # print(os.remove('filename.txt'))


# #dt module
# from datetime import datetime as dt
# now = dt.now()
# print(now)
# today=dt.today().date()
# print(today)
# time=dt.now().time()
# print(time)


# from datetime import timedelta
# delta=timedelta(days=5)
# fut_date=dt.now()+delta
# print(fut_date)

# now=dt.now()
# print(now.strftime("%d|%m|%Y"))


# #Generate random date within last 30 days
# import random 
# days_ago=random.randint(0,30)
# rand_date=dt.now()-timedelta(days=days_ago)
# print("Random date: ", rand_date.strftime("%d|%m|%Y"))


# # dir():object
# s="Hello World!"
# print(dir(s))

# import os
# print(dir(os))

# num=30
# print(dir(num))


# '''
# 1. Calculate the difference between two days 2024-01-01 and the current date print no of days
# '''

# from datetime import datetime
# fixdate = datetime(2024, 1, 1)
# curr_date=datetime.now()
# diff=curr_date-fixdate
# print(diff.days)


# '''
# Takes a date input 

# '''

# from datetime import datetime
# date_input=input("Enter the date : ")
# date_obj = datetime.strptime(date_input, "%Y-%m-%d")
# day_name=date_obj.strftime("%A")
# print(f"{day_name}")


# '''
# Checks wheather the given year is leap year
# '''
# from datetime import datetime
# year = int(input("Enter year"))
# if(year%4==0 and year%100 != 0) or (year % 400 == 0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not a leap year")
    
    
    
'''
Calculate the number of weeks between two dates the input should be in the format YYYY-MM-DD
'''
from datetime import datetime
date1 = input("Enter Date 1: ")
date2 = input("Enter Date 2: ")
date1_obj = datetime.strptime(date1, "%Y-%m-%d")
date2_obj = datetime.strptime(date2, "%Y-%m-%d")
diff=abs((date2_obj-date1_obj).days)
weeks=diff//7
print(f"No of weeks between {date1} and {date2} is {weeks} weeks")


'''
Program to display a countdown from a given date to the current date in days, hours, mins, and seconds 
'''

