 #Write a program that takes a number(n) from user 
#and prints multiplication table of n.

start = 1
end = 10
i = start
num = int(input('Enter a number:'))
while i <= end:
    print(f'{num} * {i} = {num * i}')
    i = i + 1