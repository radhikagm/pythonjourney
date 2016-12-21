"""Create a dictionary and perform some modifications to it"""

birthmonths = {

    'Radhila' : 'August',
    'Akash' : 'March',
    'Anjali' : 'Jan',
    'Saahil' : 'April'
}

print('Anjali\'s birth month is:', birthmonths['Anjali'])

del birthmonths['Radhila']

print('The number of contents in the dictionary is:', (len(birthmonths)))

birthmonths['Preeti'] = 'Feb'
birthmonths['San'] = 'July'

for x,y in birthmonths.items():
    print('Wish {} in {}'.format(x,y))
