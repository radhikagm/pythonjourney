"""Create a tuple and perform some modifications to edit the tuple"""

todo = ('exercise', 'study', 'play')

print('Number of things to do', len(todo))

new_todo = 'write', 'paint', todo

print('Number of things to do is', len(new_todo))

print('All things to do are', new_todo)

print('Things to do from old list are', new_todo[2])

print('Last thing to do is:', new_todo[2][2])

print('Number of thing to do is',
      len(new_todo)-1+len(new_todo[2]))
