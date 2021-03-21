def inverse(number):
    while number>0:
        x = number % 10
        y = number // 10
        number = y
        print x
        
a=inverse(112300)