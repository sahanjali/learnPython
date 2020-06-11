# write a program that takes input a,b from user 
# and prints the (a+b) whole square

a = float(input('Enter a number(a):'))
b = float(input('Enter a number(b):'))
whole_square = (a*a + 2*a*b + b*b)
print(whole_square)