# Creator JM 12/12/22

def get_sum(num1, num2): # get sum of 2 numbers
    return num1 + num2

def print_receipt(total): # print a friendly receipt
    return (f'the total price of your items is ${total}')

def check_out_two_items(price1, price2): # put it all together
    return print_receipt(get_sum(price1, price2))

print(check_out_two_items(11, 22) == 'the total price of your items is $33') # true
print(check_out_two_items(111, 222) == 'the total price of your items is $333') # true
print(check_out_two_items(-10, 40) == 'the total price of your items is $30') # true
print(check_out_two_items(11, 22) == 'the total price of your items is $330') # false