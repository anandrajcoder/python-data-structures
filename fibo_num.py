import numpy as np 


N = np.arange(1,10)

sqrt_5 = np.sqrt(5)

phi=(1+sqrt_5)/2

fib = np.rint((phi ** N -(-1 /phi) ** N) /sqrt_5)

print("Fib",fib)

#print(sqrt_5)
#print (phi)


 
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print Fibonacci(4)

