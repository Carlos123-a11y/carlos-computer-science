numbers = []
print('enter numbers one at a time. type Q to finish:')
while True:
    user_input =  input('enter a number(or q to finish):')
    if user_input.lower =='q':
        break
    if user_input.isdigit():
        numbers.append(int(user_input))
    else:
        print('please enter a number')
            
if len(numbers) >0:
    print(f"Numbers: {numbers}")
    
    mean = sum(numbers) / len(numbers)
    print('mean', mean)
    
    numbers.sort()
    n = len(numbers)
    if n % 2 ==1:
        median=numbers[n//2]
        
    else:
        median = (numbers[n // 2 -1] + numbers[n // 2] / 2)
        print('median', median)
        
        
mode = None
maax_count = 0
for num in numbers:
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        mode = num
    if max_count ==1:
        print('mode:No mode (all numbers occur once)')
    else:
        print('mode:' , mode)
else:
    print('No numbers entered.')
        