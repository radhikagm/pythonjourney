#!/Users/Radhika/Documents/Udemy/anaconda/bin/python

"""
  WAF to return the max of two numbers. 
  
  define the function prototype
  max(a, b)
"""


def max(a,b):
 print("The value of a is", a)
 print("The value of b is", b)
 if (a > b):
  return a
 elif (a < b):
  return b
 else :
  return a


a = 10
b = 20

value = max(a,b);

print(value)