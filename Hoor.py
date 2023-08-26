my_name=input('what is your name?')
my_age=input('what is your age?')
print(f'my name is {my_name} and I am {my_age} years old')

first_number=input('choose the first number')
second_number=input('choose the second number')
operation=input('choose a sign to do the operation')
if operation=='+':
    print(first_number+second_number)
elif operation=='-':
    print(first_number-second_number)
elif operation=='*':
    print(first_number*second_number)
elif operation=='/':
    print(first_number/second_number)
else:
    print('the operation is not valid')

bus_capacity=40
people_inbus=int(input('how many people is in the bus?'))
waiting=int(input('how many people are waiting?'))
empty_seats = bus_capacity - people_inbus
if empty_seats>=waiting :
    print('join!')
else:
    print('oops the bus is full')
