#!/Users/Radhika/Documents/Udemy/anaconda/bin/python

"""WAP that prints the numbers from 1 to 100, but 
 - for multiples of 3 print “Fizz” instead of the number and
 - for the multiples of 5 print “Buzz” and
 - for numbers which are multiples of both 3 and 5 print “FizzBuzz”"""
 
for x in range (1,100+1):
    if ((x % 3) == 0) and ((x % 5) == 0):
      print("FizzBuzz")
    elif ((x % 5) == 0):
      print("Buzz")
    elif ((x % 3) == 0):
      print("Fizz")
    else:
      print(x)