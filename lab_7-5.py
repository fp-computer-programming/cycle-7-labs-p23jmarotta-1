# Creator JM 12/12/22

# Lab 6-5
print('Lab 6-5 --------')

def highs_and_lows(list):
    list.sort()

    if len(list) <= 2 or list[-1] == list[0]:
        return ('error: list does not meet specifications')
    else:
        return (f'Highest: {list[-1]}, lowest: {list[0]}')

print(highs_and_lows([0,1,2,3,4]) == "Highest: 4, lowest: 0")
print(highs_and_lows([0,0]) == "error: list does not meet specifications")
print(highs_and_lows([-123,1,912,5,4234]) == "Highest: 4234, lowest: -123")
print(highs_and_lows([0,1,2,3,4*2]) == "Highest: 8, lowest: 0")


# Lab 6-6
print('Lab 6-6 --------')

def word_length_finder(word1, word2, word3, word4, word5):
    return [len(word1), len(word2), len(word3), len(word4), len(word5)]

print(word_length_finder('Joe', 'Apple', 'Car', 'Alphabet', 'Zoo') == [3,5,3,8,3])
print(word_length_finder('Joey', 'Apples', 'Cars', 'Alphabets', 'Zoos') == [4,6,4,9,4])
print(word_length_finder('hisdfisdf', 'woooo', 'yeee', 'wooooo', 'skewww') == [3,5,3,8,3])
print(word_length_finder('Christmas', 'holiday', 'LIGHTS', 'santa', 'gifts') == [9,7,6,5,5])


# Lab 6-7
print('Lab 6-7 --------')

def number_doubler(numbers):
    return [numbers[0] * 2, numbers[1] * 2, numbers[2] * 2] # Double each value

print(number_doubler([0,1,2]) == [0,2,4])
print(number_doubler([0,32,64]) == [0,64,128])
print(number_doubler([0,1,2]) == [0,234725823,4])
print(number_doubler([0,1,2]) == [1,2,4])

# Lab 6-8
print('Lab 6-8 --------')

def even_odd_checker(one, two, three):
    # Check if they are odd or even using modulus 2
    if one % 2 == 0 and two % 2 == 0 and three % 2 == 0: # This would be a great place for a loop
        return ('even')
    elif one % 2 == 1 and two % 2 == 1 and three % 2 == 1:
        return ('odd')
    else: # If they aren't all even or odd they must be mixed
        return ('mixed')

print(even_odd_checker(2,2,2) == 'even')
print(even_odd_checker(3,3,3) == 'odd')
print(even_odd_checker(2,3,2) == 'mixed')
print(even_odd_checker(-2,-3,-22345) == 'mixed')
