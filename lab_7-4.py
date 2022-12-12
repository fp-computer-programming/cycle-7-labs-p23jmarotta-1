# Creator JM 12/7/22

def find_sum(num1, num2):
    num_sum = num1 + num2
    return num_sum

my_sum = find_sum(111,222)

print(find_sum(111,222) == 333) # True
print(find_sum(111,222) == '333') # False
print(find_sum(131,232) == 363) # True
print(find_sum(23423,2352351234) == 12) # False