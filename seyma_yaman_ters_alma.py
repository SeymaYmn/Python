def inverse(number):
    a = 0
    while number>0:
        x = number % 10
        y = number // 10
        number = y
        a = 10*a + x
    return a
        
a=inverse(12347272)
print a