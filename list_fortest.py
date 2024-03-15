pizzas=['pizza1','pizza2','pizza3']
for pizza in pizzas:
    print(f'I like {pizza}.\n')
print('I really like pizza! \n')

animals=['cat','dog','pig']
for animal in animals:
    print(f'A {animal} would make a great pet. \n')
print('Any of these animals would make a great pet!')

animals=['cat','dog','pig','monkey','tiger'] 
print('The first three items in the list are:')                                                      
for animal in animals[0:3]:
    print(animal)
print('Three items from the middle of the list are:')                                                      
for animal in animals[1:4]:
    print(animal)
print('The last three items in the list are:')                                                      
for animal in animals[2:]:
    print(animal)

my_pizzas=['pizza1','pizza2','pizza3']
friend_pizzas=my_pizzas[:]
my_pizzas.append('pizza4')
friend_pizzas.append('pizza5')
print('My favourite pizzas are:')
for pizza in my_pizzas:
    print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)