#Write a program that takes a number n from user 
#and prints the sum of all natual number from 1 to n.

start = 1
end = int(input('enter a number:'))
i = start
sum = 0
while i <= end:
    sum = sum + i
    i = i + 1
print(sum)    
