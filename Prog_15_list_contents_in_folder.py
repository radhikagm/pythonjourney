"""Create a new folder """

import os

path = '/Users/Radhika/Documents'

dirs = os.listdir( path )

for file in dirs:
   print (file)


