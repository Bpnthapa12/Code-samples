# This python program is used to swap the value to two number without using third variable.
first_number = int(input("Enter your first number:- "))
second_number = int(input("Enter you second number:- "))
print(f'Below is the first and second number before swaping the value')
print(first_number,second_number)
first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number
print(f'Below is the first and second number after swaping the value')
print(first_number,second_number)
