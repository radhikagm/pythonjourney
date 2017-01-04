filename = '/Users/Radhika/Desktop/Demo.txt'

with open(filename) as f:
    lines = f.readlines()


for x in lines:
    print (x)
