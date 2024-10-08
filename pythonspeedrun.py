print ("hello world")

for i in range (1, 6):
    print(i)

variable = "this text var"
print(variable)

name = "rossivel aqUino"
print("title:", name.title())
print("upper:", name.upper())
print("lower:", name.lower())

first_name = "rossivel"
last_name = "aquino"
full_name = first_name + " " + last_name
print("full name:", full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message) 

print("\tTab")

print("Languages:\nPython\nC\nJavaS.")
      
print("Languages:\n\tPython\nC\n\t\tJavaS.")

fav_lan = 'python '
print(fav_lan.rstrip())

fav_lan = ' python'
print(fav_lan.lstrip())

fav_lan = ' python '
print(fav_lan.strip())
 
#2-3 / 2-7 exercises

new_name = "carlos"
print("want to learn some pythong", new_name)

print(full_name.title(), "quote")

famous_person = "mark zuk"
message = famous_person + " quoty quote quote quote"
print (message)

print(3 + 3)
print(2 - 2, 2 * 2, 2 / 2)

print(3 ** 2, 3 ** 3, 10 ** 2)

print((2+3) ** 5)

age = 15
message = "happy " + str(age) + 'rd Birday!'
print(message)

#list 

bicycles = ['trek', 'cannon', 'redline', 'special']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
#-2 second item from the end and so on, good for when we want to access
#the final item in a list

message = "My first bike was a " + bicycles[2].title()
print(message)

#3-1 to 3-3
friends = ['carlos', 'seba', 'tavo']
print(friends[0], friends[1], friends[-1])

message = 'sup ' + friends[1].title() + ' you pussy'
print(message)

transport = ['car', 'moto', 'train']
message = 'i like ' + transport[1] + 's'
print(message)

#changing and adding elements to a list

print(transport)

transport[0] = 'airplane'
print(transport)

transport.append('car')
print(transport)

new_transport = []
new_transport.append('boat')
new_transport.append('helicopter')
new_transport.append('balloons')
print(new_transport)

#inserting elements into a position in the list
#removing elements from the list

new_transport.insert(1, 'kite')
print(new_transport)

del new_transport[1]
print(new_transport)

#removing with del or pop() differences
#pop allows you to use the item you just "popped" unlike delete which gets
#rid of it completly, pop takes the last item (can be out of any spot)

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

popped_motos = motos.pop()
print(motos)
print(popped_motos)

last_owned = motos.pop(0)
print('the last moto i had was ' + last_owned)

print(motos)

#you may want to remove an item based on the value, we can use remove()
#will only remove the value once from a list if it is in it more than once
#loop required to get rid of all

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

motos.remove('honda')
print(motos)

motos.append('ducati')

too_expensive = 'ducati'
motos.remove(too_expensive)
print(motos)
print('\nA ' + too_expensive.title() + " is too expensive")
 
#3-4 too 3-7 

guests = ['zoro', 'nami', 'robin'] 
print('come to la fiesta my n ' + guests[0].title(), guests[1].title() + " and " + guests[-1].title())
print('i heard ' + guests[0].title() + ' cant make it')

guests.remove('zoro')
guests.append('franky')

print('u better come to la fiesta my n ' + guests[0].title(), guests[1].title(), guests[-1].title())

guests.insert(0, 'chopper')
guests.insert(3, 'luffy')
guests.append('sanji')

print(guests)

print('yo bigger table going here now u better come ' + guests[0].title(), guests[1].title(), guests[2].title(), guests[3].title(), guests[-2].title() + " and " + guests[-1].title())


print('no table gotta let yall go, only two can come and thats the ladies ' + guests[0].title(), guests[1].title(), guests[-1].title())

print('bye' + guests.pop(-1))
print('bye' + guests.pop(-1))
print('bye' + guests.pop(-1))
print('bye' + guests.pop(0))

print('yall still coming tho ' + guests[0].title(), guests[1].title())

del guests[0]
del guests[0]

print("this is the list now: " + str(guests))


#sorting list permanently with sorth()
#reverse order as well sort(reverse=True) or reverse()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#sorted(), maintain original order f list but presented sorted

print('original list ' + str(cars))
print('sorted list ' + str(sorted(cars)))
print('sorteted list ' + str(cars.sort()))
print('og list again ' + str(cars))

cars.reverse()
print(cars)

#find length of a list
print(len(cars))


places = ['france', 'albania', 'india', 'spain', 'china']
print('1 \n')
print(places)

print('2 \n')
print(sorted(places))

print('3 \n')
print(places)

print(sorted(places, reverse=True))
print('4 \n')
print(places)

places.reverse()
print('5 \n')
print(places)

places.reverse()
print('6 \n')
print(places)

places.sort()
print('7 \n')
print(places)

places.sort(reverse=True)
print('8 \n')
print(places)

magicians = ['alice', 'harry', 'luis']
for magician in magicians:
    print(magician.title() + ", what a great trick")
    print("\nCant wait to see your next trick, " + magician.title())

print("thanks to all the magicians")

#tip use singular and plural in for loops in order for better readability

pizzas = ['peperoni', 'cheese', 'chorizo']
for pizza in pizzas:
    print("i like " + pizza.title() + " pizza")
print('I really love pizza')

animals = ['cat', 'dog', 'cow']
for animal in animals:
    print(animal.title() + ' would make a great pet')
print('all these animals have 4 legs')

#range() list()

for value in range(1,5):
    print(value)


numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    #^^^ squares.append(value**2)
print(squares)

#List Comprehensions:
squares = [value**2 for value in range(1,16)]
print(squares)
digits = [1, 2, 3, 4, 5, 6]

print(min(digits))
print(max(digits))
print(sum(digits))

#4-3 to 4-9

print('\n4-3')
for value in range(1,21):
    print(value)

print('\n4-4')
million = list(range(1,51))
print(million)

print('\n4-5')
print(min(million))
print(max(million))
print(sum(million))

print('\n4-6')
for value in range(1,21,2):
    print(value)

print('\n4-7')
for value in range(3,31,3):
    print(value)

print('\n4-8')
for value in range(1,10):
    print(value**3)

print('\n4-9')
cube = [value**3 for value in range(1,10)]
print(cube)

players = ['carlos', 'seba', 'andy', 'tavo']
#prints slice of list
print(players[0:2])

#this starts at position 4 and gives you all there is after taht position
print(players[3:4])

#omiting the beginning, starts at the beginning till second number end
print(players[:3])

#omiting the end, starts at 1st number till end, 
# this case (if you want items from 2 onward)
print(players[1:])

#output the last ppl in the list
print(players[-2:])

#output the first ppl in the list
print(players[:-2])

#makes a copy of the list by starting at each end
print(players[:])

print("first three players ")
for player in players[:3]:
    print(player.title())

food = ['pizza', 'burger', 'fries']
friend_food = food[:]

food.append('lasagna')
friend_food.append('ice cream')

print('my fav foods are ' + str(food))
print('my friends fav food are ' + str(friend_food))


books = ['harryp', 'onep', 'jjba', 'jjk', 'mobp', 'vinland', 'naruto']
print('first three items of the list are ' + str(books[:3]))

print('list from the middle ' + str(books[2:]))

print('last three in the list ' + str(books[-3:]))

my_pizza = ['pepper', 'onion', 'cheese']
friend_pizza = my_pizza[:]

my_pizza.append('sausage')
friend_pizza.append('pineapple')

print('my fav pizzas are ')
for pizza in my_pizza[0:]:
    print(pizza.title())

for pizza in friend_pizza[0:]:
    print(pizza.title())

#Lists that cant change (Immutable) or TUPLES

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# dimensions[0] = 250 
#this line ^ gives us an error since we're trying to change a tuple

for dimension in dimensions:
    print(dimension)

#only way to "rewrite" a tuple is by overwriting the varible

dimensions = (400, 100)
print(dimensions[0])
print(dimensions[1])

buffets = ('pizza', 'burger', 'taco', 'salad', 'bbq')
for buffet in buffets:
    print(buffet)

#error no rewritting --- buffets[0] = 'cake'

buffets = ('cake', 'burger', 'taco', 'ice cream', 'bbq')
for buffet in buffets:
    print(buffet)



# if and else
cars = ['kia', 'audi', 'bmw', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

car = 'Audi'
print(car == 'audi')

print(car.lower() == 'audi')

# Inequality - !=

topping = 'mushrooms'
if topping != 'anchovies':
    print("hold the anchovies")

#can be numerical

age = 19
print(age == 19)

#can also use other mathematical operations & multiple conditions
# >
# <
# <=
# >=

age1 = 19
age2 = 24

#and \ or

print(age1 == 19 and age2 > 25)
print(age1 == 19) and (age2 > 22)

print(age1 >= 19) or (age2 > 25)
print(age1 > 20 or age2 < 22)

requested_toppings = ['mushrooms', 'sausage', 'onions']
print('mushrooms' in requested_toppings)

banned_users = ['carlos', 'seba', 'tavo']
user = 'marie'

if user not in banned_users:
    print(user.title() + ' youre able to post if ud like')

#Booleans

game_weather = True
can_edit = False

#5-2
car = 'toyota'
print(car == 'toyota')
print(car != 'honda')
print(car != 3)

car2 = 'toyota'
cars = 5000

print(car == car2)

print((cars < 6000) and (car == 'toyota'))


car = 'SUZUKI'

print(car.lower() == 'suzuki')

baths = ['pipi', 'popo', 'pupu']
bath = 'papa'
if bath in baths:
    print('you may ' + bath.upper() + ' in the bathroom')
else:
    print('please dont ' + bath.upper() + ' here')

# if elif else
#good for multiple conditions
#bad if we need it to go through each line to print or verify data

age = 93

if age == 15:
    print("you may get your permit")
elif age == 16:
    print('you may get your license')
elif age > 85 and age < 99:
    print('you shouldnt be driving, were taking your license away')
elif age > 100:
    print('youre alive?')
else:
    print('you may not get your permit')


#5-3 to 5-7

aliens_color = ['green', 'yellow', 'red']
alien_color = 'green'

if alien_color == 'green':
    print('you earned 5pts')
elif alien_color == 'yellow':
    print('you earned 10pts')
elif alien_color == 'red':
    print('you earned 15pts')
else:
    print('INFINITE POINTS')


age = 99

if age < 2:
    print('ur a baby')
elif age >= 2 and age < 4:
    print('ur a toddler')
elif age >= 4 and age < 13:
    print('ur a kid')
elif age >= 13 and age < 19:
    print('ur a teenager')
elif age >= 20 and age < 65:
    print('ur an adult')
elif age >= 65 and age <= 99:
    print('ur an elder')
elif age >= 100:
    print('nah fam u dead')

"""
fav_fruits = ['kiwi', 'apple', 'banana', 'grapes']
fruit = str(input())
if fruit == 'kiwi':
    print('u really like kiwis')
elif fruit == 'apple':
    print('u really like apple')
elif fruit == 'banana':
    print('u really like banana')
elif fruit == 'grapes':
    print('u really like grapes')
else:
    print(fruit.title() + ' never heard of that fruit')
"""

requested_toppings = ['peperoni', 'pineapple', 'sausage', 'green peppers']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('we outta those b')
    else:
        print('Adding ' + requested_topping + '.')
print('pizzas ready')

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('we outta those b...')
        else:
            print('Adding ' + requested_topping + '.')
    print('pizzas ready...')
else:
    print('nothign on the pizza g?')

#multiple lists

available_toppings = ['mushrooms', 'olvies', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we don't have " + requested_topping + ".")
print("pizzas ready s...")

#5-8 too 5-13

usernames = ['frank', 'death', 'mouse', 'book', 'sword', 'admin']
if usernames:
    for username in usernames:
        if username != 'admin':
            print('Hello ', username + '.')
        else:
            print("Status report admin?")
    print('go play :)')
else:
    print('no games today...')

usernames = []
if usernames:
    for username in usernames:
        if username != 'admin':
            print('Hello ', username + '.')
        else:
            print("Status report admin?")
    print('go play :)')
else:
    print('no games today...')


#REVIEW NOT WORKING PROPERLY

'''current_users = ['block', 'mouse', 'rat', 'cOw', 'boom', 'LEVI']
new_users = ['bat', 'store', 'happy', 'cow', 'lead', 'Levi']

if current_users:
    if new_users:
        for new_user in new_users:
            if new_user.lower() and new_user.upper() in current_users:
                print(new_user + " is unavailable, try again...")
            else:
                print(new_user + " is available.")
    else:
        print('bye bye')
else:
    print("goodbye")'''

current_users = []
new_users = ['bat', 'store', 'happy', 'cow', 'lead', 'Levi']

if current_users:
    if new_users:
        for new_user in new_users:
            if new_user.lower() and new_user.upper() in current_users:
                print(new_user + " is unavailable, try again...")
            else:
                print(new_user + " is available.")
print("goodbye")    
