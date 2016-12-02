#!/Users/Radhika/Documents/Udemy/anaconda/bin/python

"""
WAP to print Fibonacci series between 0 to N. 

"""

print("Enter the value of N")
N = int(input())
print("The value of N is", N) 

a = 0
b = 1
  
for x in range (0,N):
  c = a + b
  a = b
  b = c
  print(c)
  