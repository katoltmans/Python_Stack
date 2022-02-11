#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#Output prediction: 5  Answer:  correct


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Output prediction: None  Answer:  NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined - error, not None


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Output prediction: 5  Answer:  correct


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Output prediction:  5 10  Answer:  5 - Only prints the return


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Output prediction: 5  Answer:  5, None - Parameters were not passed through the function when called


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Output prediction: 8  Answer:  3, 5, TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType' - Prints b and c instead of adding - function never adds values together, just concatenates


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Output prediction: 2, 5  Answer:  25 - concatinating treats strings as characters and adds them together - 


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# #Output prediction: 100, 10  Answer: correct


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Output prediction: 7, 14, 21  Answer:  correct


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Output prediction: 8  Answer:  correct


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Output prediction: 500, 500, 300, 500  Answer:  correct


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Output prediction: 500, 500, 300, 500  Answer:  correct


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Output prediction: 500, 500, 500  Answer:  500, 500, 300, 300 - Will print the 300 because B was changed to the function (prints and returns to print)


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#Output prediction: 1, 3, 2  Answer:  correct


15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Output prediction: 1, 3, 5, 10  Answer:  correct