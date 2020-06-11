# write a program that takes input P, T, R from user 
# and prints the simple interest

p = float(input('Enter principle amount(P):'))
t = float(input('Enter time in  years(T):'))
r = float(input('Enter rate (R):'))
simple_interest = (p * t * r)/ 100
print(f'Simple interest amount is {simple_interest}')
