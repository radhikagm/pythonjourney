#!/Users/Radhika/Documents/Udemy/anaconda/bin/python

N = int(input("Please Enter any Number: "))
Sum = 0
 
while(N > 0):
    last_digit = N % 10
    Sum = Sum + last_digit
    N = N //10
    
print("Sum of the digits of the given number is", Sum)
 

