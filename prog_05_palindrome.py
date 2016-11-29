#!/Users/Radhika/Documents/Udemy/anaconda/bin/python

N = int(input("Please Enter any Number: "))

Number = N

Reverse = 0

while(N > 0):
    last_digit = (N % 10)
    Reverse = (Reverse *10) + last_digit
    N = (N // 10)
    
print("Reverse of entered number is", Reverse)
 
if (Reverse == Number):
  print("Number is a palindrome")
else:
  print("Number is not a palindrome")

