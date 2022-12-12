# Creator JM 12/7/22

def greeting():
    ''' This will print hello world on 1 line, thats all'''
    return('Hello, World!')
    #return help(greeting)

print(greeting())

print(greeting() == 'Hello, World!') # True
print(greeting() == 'Hello, Joe!') # False
print(greeting() == 'hello, world!') # False
print(greeting() == '283472342356') # False
