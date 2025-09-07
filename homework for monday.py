'''

user1=input('enter your name:')
name=user1
print(user1)
user2=input('enter your second name:')
print('hello',user1,user2)
#2
number_input1=int(input('enter a number:'))
number_input2=int(input('enter a number:'))
print(number_input1 + number_input2)

#3
number1=int(input('enter a number:'))
number2=int(input('enter a number:'))
number3=int(input('enter a number:'))
part1=(number1 + number2)
number4=part1
part2=(number3 * part1)
print('the answer is',part2)

#4
pizza_number=int(input('how many slices of pizzas did you start with?:'))
pizza_ate=int(input('how many did you eat?:'))
eaten=(pizza_number - pizza_ate)
print(eaten)

#5
user_name=input('what is your name:')
user_age=int(input('how old are you:'))
next_year=(user_age +1)
print('hello',user_name ,'next year you will be',next_year)
'''
#6
user_bill=int(input('how much was the bill:'))
user_people=float(input('how many diners were there:'))
answer=(user_bill / user_people)
print('you each have to pay', answer)
