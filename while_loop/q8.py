#8. Write a program that prints 
#multiplication table for all number from 1 to 10

start = 1
end = 10
table_i = start
while table_i <= end:
    print(f"Table for {table_i}")
    mul_start = 1
    mul_end = 10
    mul_i = mul_start
    while mul_i <= mul_end:
        print(f'{table_i} * {mul_i} = {table_i * mul_i}')
        mul_i = mul_i + 1
    table_i = table_i + 1


