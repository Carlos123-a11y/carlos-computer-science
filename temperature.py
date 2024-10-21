'''
#1
day1 =  int(input('temperature on day one:'))
day2 = int(input('temperature on day 2:'))
day3 = int(input('temperature on day 3:'))
day4 = int(input('temperature on day 4:'))
day5 = int(input('temperature on day5:'))
day6 = int(input('temperature on day 6:'))
day7 =  int(input('temperature on day 7:'))
average = day1 + day2 + day3 + day4 + day5 + day6 + day7
print(average/7)

#2
PI=3.14
x=int(input('enter X value:'))
y=int(input('enter Y value:'))
z=int(input('enter Z value:'))
print(4*x**4 + 3*y**3 + 9*z + 6*PI)
#3
seconds=int(input('enter an amount of seconds'))
min = seconds//60
sec=seconds %60
print(min,seconds)
#4
user_time=int(input('type an hour between 1 and 12:'))
user_time2=int(input('how many hours ahead would you like to know the time:'))
timeahead= user_time+user_time2
print(timeahead,'oclock')
'''
#5
threedigit = int(input("enter a three digit number"))
firstdigit = threedigit%10
seconddigit = threedigit//10
third = seconddigit//10
fourth = seconddigit%10
print(firstdigit , fourth,third, sep="")
#6
day = int(input('enter a day:'))
month = int(input('enter a month:'))
total = day*30
totals = total+month
print(totals)
