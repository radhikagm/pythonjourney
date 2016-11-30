#!/Users/Radhika/Documents/Udemy/anaconda/bin/python

#Using functions 
N = int(input("Please Enter any Number: "))
  
def is_palindrome():
  global N
  Number = N
  Reverse = 0

  while(N > 0):
      last_digit = (N % 10)
      Reverse = (Reverse *10) + last_digit
      N = (N // 10)
    
  #print("Reverse of entered number is", Reverse)
 
  if (Reverse == Number):
  	return True
  else:
    return False

#end of function

#Function Call

a = is_palindrome()
print(a)

if(a == True):
  print('Is a palindrome')
else:
  print('Not a palindrome')

