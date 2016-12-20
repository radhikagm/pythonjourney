""" Create a tour itinerary using a list. Perform the following functions:
1. Print int lenght of the list
2. Print the list
3. Add an item
4. Sort the list
5. Delete an item
6. Print the final list"""

#List of places to visit in California


places = ['SF,', 'LA,', 'SD,', 'Yosemite National Park,', 'Anaheim,', 'Napa Valley,', 'Palm Springs,', 'Santa Barbara,', 'Big Sur,', 'Lake Taho,']

print('I have', len(places), 'places to visit in California')

print('These items are:', end=' ')
for item in places:
    print(item, end=' ')

print('\nI also want to visit.')
places.append('Carmel')
print('My list is now', places)

print('The places in alphabetical order are')
places.sort()
print('Sorted list is', places)

print('The first place I visited was', places[0])
olditem = places[0]
del places[0]
print('Since I visited the following places', olditem)
print('My list is now', places)

#Referenc: https://python.swaroopch.com/data_structures.html
