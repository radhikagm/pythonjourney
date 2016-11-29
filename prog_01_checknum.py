#!/Users/Radhika/Documents/Udemy/anaconda/bin/python

"""WAP to get a number from a user, and display 
     - if it is positive or negative
     - if it is Odd or Even. 
     - if it is Prime or Composite"""
     

#function to check if input is an integer
def is_integer(inputstr):
  # check if input is an Integer
  ## check if first character is +, - or numeric
  ## check if remaining string is numeric using str.isdigit()

  a = inputstr[0]
  #print(a)
  b = inputstr[1:]
  #print(b)

  if (((a == '-') or (a == '+') or (a.isdigit())) and (b.isdigit()) or b==''):
    return True
    #print("Input is an Interger")
  else:
    return False
    #print("Input in not an integer, quitting")

  
# get input from user
inputstr = input("Enter the Number: ")

# print the input
print('The number entered is', inputstr)

x = is_integer(inputstr)
print(x)

if (x == False):
   print("Input in not an integer, quitting")
   exit()
  
number = int(inputstr)

#Check if number is positive or negative 

if (number > 0):
  print(number, 'is Positive')
elif (number < 0):
  print(number, 'is Negative')
else:
  print(number, 'is Zero')

#Check if even or odd

if (number % 2 == 0):
  print(number, 'is Even')
else:	
  print(number, 'is Odd')
	   
#Check if number is Prime or composite

is_composite = False

#if (number == 1) or (number <= 0):
  #print(number, 'is neither Prime nor Composite')
  #break

if (number > 1):
  for x in range (2, number - 1):
      if (number % x == 0):
        is_composite = True	
        break     

  if (is_composite == True):
    print(number, "is Composite")
  else:
    print(number, "is Prime")   
else:
  print(number, 'is neither Prime nor Composite')
