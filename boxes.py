import math as m

#I made this alternative prime test.
#Right now, it is not perfect.
#It seems to think numbers divisible by 5 are prime
#This program is unfinished.
#It currently only does numbers 5 mod 6.

def is_integer(n):
    return isinstance(n, float) and n.is_integer()

test_num = int(input("Enter number to check: "))
#test_num = 10*1000000 + 1
mod6 = test_num % 6
prime = True


if test_num == 2 or test_num == 3:
    prime = True
elif mod6 == 2 or mod6 == 3 or mod6 == 4:
    prime = False
elif mod6 == 1:
    box_num = (test_num - 1)/3
    print(box_num)
elif mod6 == 5:
    box_num = (test_num - 2)/3
    #prime_chckr = True
    #6*u*(u - x) + 4*(u - x) + u
    #6*x*u + 5*u
    #-4*x - x = -5*x
    #x is the box number.
    
    for x in range(0, 6*m.floor(m.sqrt(test_num))):
        if test_num % 5 == 0 and test_num != 5:
            print(False)
            break
        step = -6*x + 5
        #print("step: ")
        #print(step)
        u = (-step + m.sqrt(step**2 - 24*(-box_num - 4*x)))/12
        #print("u: ")
        #print(u)
        if is_integer(u) and u != box_num:
            print(u)
            #prime = False
    
    #print(prime)
    
    
            
            