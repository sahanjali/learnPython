# write a program that takes a character(a-z) and 
# prints if it is vowel or consonant
# bonus point if ternary operator is used.

character = input('Enter a character:')
if character in ['a', 'e', 'i', 'o', 'u']:
    print('Your character is vowel')
else:
    print('Your character is consonant')    


# alternative -1
character = input('Enter a character:')
if character  == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print('Your character is vowel')
else:
    print('Your character is consonant')   
 