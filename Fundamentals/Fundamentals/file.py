num1 = 42 #variable declaration, integer
num2 = 2.3 #variable declaration, float
boolean = True #variable declaration, Boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #prints blueberry, strawberry, bananna
print(pizza_toppings[1]) #prints Sausage
pizza_toppings.append('Mushrooms') #add mushrooms to the end of the pizza_toppings list
print(person['name']) #prints John
person['name'] = 'George' #change John to George in the person dictionary
person['eye_color'] = 'blue'#add eye color to the person dictionary
print(fruit[2]) # prints banana

if num1 > 45: #if conditional for values greater than 45
    print("It's greater") #action to be taken if condition is true
else: #else conditional for all other values
    print("It's lower") #action to be taken if condition is true - this one will print

if len(string) < 5: #if conditional for values less than 5
    print("It's a short word!") #action to be taken if condition is true
elif len(string) > 15: #else if conditional for values greater than 15
    print("It's a long word!") #action to be taken if condition is true
else: #else  conditional for all values between 5 - 15
    print("Just right!") #action to be taken if condition is true - this one will print

for x in range(5): #forloop that creates a sequence of numbers from 1-4
    print(x) # prints 01234 on separtate lines
for x in range(2,5): ##forloop that creates a sequence of numbers from 2-4
    print(x) # prints 234 on separtate lines
for x in range(2,10,3): #forloop that creates a sequence of numbers from 2-9 but increments by 3 instead of 1
    print(x) # prints 258 on separtate lines
x = 0 #variable declaration, while loop start
while(x < 5): #while loop that prints x as long as x is less than 5 - stops at 4
    print(x) # prints 01234 on separtate lines
    x += 1 #increments up one each time the loop runs

pizza_toppings.pop() #deletes olives from the pizza toppings list
pizza_toppings.pop(1) #deletes sausage from the pizza toppings list

print(person) #prints {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') #deletes eye color from the person dictionary
print(person) ##prints {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings: #for loop that iterates through pizza toppings
    if topping == 'Pepperoni': #conditional if the value equals pepperoni
        continue #will continue through the for loop
    print('After 1st if statement') #prints string 'after 1st if statement 3 times for the first three ingredients
    if topping == 'Olives': #conditional if the value equals olives
        break #current loop terminates - will not print for olive position

def print_hello_ten_times(): #defines function print_hello_ten_times
    for num in range(10): #forloop that iterates through the loop according to the number provided (ten times in this case)
        print('Hello') # will print hello ten times when called

print_hello_ten_times() #calls the print_hello_ten_times function and prints hello ten times on separate lines

def print_hello_x_times(x): #defines function print_hello_ten_times
    for num in range(x): #will iterate through the for loop x times if x is defined
        print('Hello') # will print hello a given number of times once x is defined

print_hello_x_times(4) #calls the print_hello_ten_times function and prints hello four times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #calls the print_hello_x_or_ten_times and prints hello ten times since x is defined as 10 within the function
print_hello_x_or_ten_times(4) #calls the print_hello_x_or_ten_times and prints hello four times


"""
Bonus section
"""

# print(num3) #error: the vairbale num3 has not been defined
# num3 = 72 #variable declaration - defines num3 - will not print since not before the above line of code
# fruit[0] = 'cranberry' #error: fruit is a tuple that cannot be changed
# print(person['favorite_team']) #error: favorite team is not defined in the person dictionary
# print(pizza_toppings[7]) # error: there are not 8 pizza toppings listed
# print(boolean) #prints true
# fruit.append('raspberry') #error: fruit is a tuple that cannot be changed
# fruit.pop(1) #error: fruit is a tuple that cannot be changed