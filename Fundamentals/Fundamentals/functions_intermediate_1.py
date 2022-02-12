#Update Values in Dictionaries and Lists - make given changes as indicated in assignment
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#Update x
x[1][0] = 15
print(x)
#Update students
students[0]['last_name'] = 'Bryant'
print(students)
#Update sports_directory
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
#Update z
z[0]['y'] = 30
print(z)

#Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for x in some_list:
        newString = ""   
        for key, val in x.items():
            newString += key + " - " + val + ", "
        print(newString[0:-2])       
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#Get Values From A List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for x in some_list:
        for key, val in x.items():
            if key == key_name:
                print(val)
        
iterateDictionary2('first_name', students)
print()
iterateDictionary2('last_name', students)

#Iterate Through A Dictionary With List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key, val in some_dict.items():
        listLength = len(val)
        print(str(listLength) + " " + key.upper())
        for x in val:
            print(x)
        print()


printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


