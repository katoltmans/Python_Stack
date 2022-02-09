#Basic - Print all integers 0-150
for x in range(0, 151):
    print(x)
    
#Multiples of Five - Print all multiples of 5 from 5-1000
for x in range(5, 1001, 5):
    print(x)
    
#Counting, The Dojo Way - Print integers 1-100 (multiples of 5 print "Coding" and multiples of 10 print "Coding Dojo")
for x in range(1, 101):
    print(x)
    if(x%10==0):
        print("Coding Dojo")
    elif(x%5==0):
        print("Coding")

#Whoa. That Sucker's Huge - Add odd integers from 0-500,000 and print final sum
sum = 0
for x in range(0, 500000):
    sum = sum + x
print(sum)

#Countdown By Fours - Print all numbers counting down by 4's starting with 2018
for x in range(2018, -1, -4):
    print(x)

#Flexible Counter - print all multiples of a given number between a range of numbers
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum,highNum +1):
    if(x%mult ==0):
        print(x)