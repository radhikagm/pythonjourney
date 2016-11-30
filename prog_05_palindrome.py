#!/Users/Radhika/Documents/Udemy/anaconda/bin/python

#Using functions 
N = int(input("Please Enter any Number: "))
  
def is_palindrome(N):
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

#end of function

#Function Call
is_palindrome(456)
is_palindrome(454)

