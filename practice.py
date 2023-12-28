# set my_number to 42. Set my_name to your name. now swap my_number into my_name and vice versa.
my_number = 42
my_name = "tenz"
print(my_number, my_name)
temp = my_number
my_number = my_name
my_name = temp
print(my_number, my_name)

# print -52 t0 1066 through For loop
for i in range(-52,1066):
    print(i)

# create a function be_cheerful(). Within it console.log string "good morning!" Call it 98 times
def be_cheerful():
    for i in range(0,99):
        i = print("good morning!")
    return i
be_cheerful()

# Using for , print multiples of 3 from -300 to 0. skip -3 and -6.
for i in range(-300,0,3):
    if i == -6:
        break
    else:
        print(i)

# print integers from 2000 to 5280, using a while
x = 2000
while x < 5280:
    print(x)
    x += 1
from itertools import product
# if 2 given numbers represents your birth month and day if either order, print"How did you know?", else print "Just another day.."
def birth_compare(month,day):
    num = int(input("What's your first number? = "))
    num2 = int(input("what's your second number? = "))
    if(num == month and num2 == day) or (num == day and num2 == month):
            print("how did you know?")
    else:
        print("just another day")
    return

birth_compare(4,5)

# Write a function that determines whether a given year is a leap year. If a year is divisible 
# four, its a leap year, unless it is divisible by 100. However, if it divisible by 400, then it is

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                print(f"{year} is a leap year!")
            else:
                print(f"{year} is not leap year")
        else:
            print("It's  leap year")
    else:
        print(f"{year} is not a leap year")
    return

leap_year(2023)

# print all integer multiples of 5, from 512 to 4096. Afterward, also print how many they were
count = 0
for i in range(512 , 4096):
    if (i % 5 == 0):
        print(i)
        count += 1
print(count)

# print multiplies of 6 up to 60,000. Using while
i = 0
while i < 60000:
    if i % 6 ==0:
        print(i)
    i += 1

# print integers 1 to 100. if divisible by 5, print "coding" instead. If by 10, also print "Dojo".
for i in range(1, 100):
    if i % 10 == 0:
        print("dojo")
    elif i % 5 == 0:
        print("coding")

state = input("What's is your state? = ")
print(f"i live in {state} state.")

# Add odd integers from -300000 to 300000 and print the final sum.

sum = 0
for i in range(-300000, 300001, 2):
    sum += i
    print(sum)




# log positives numbers starting at 2016, counting down by fours(exclude 0), without for loops
x = 2016
while x > 0:
    print(x)
    x -= 4

#Change the all the positive number in list to string in Function.
def con_to_string(list): #converting the positives numbers into strings.
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(con_to_string([-1,3,5,-5]))

#given ([2,4,6,8,10],3), change the given array to [6,8,10] and return it
def decrementing_list(list,y):
    list = list[y-1:]
    return list

print(decrementing_list([2,4,6,8,10],3))

# Kenny tries to stay safe, but somehow every day something happens. Out of the last 100 days, 
# there were 10 days with volcanos, 15 others with tsunamis, 20 earthquakes, 25 blizzards, 
# and 30 meteors(for 100 days total). if this possibilities continue , write what_happens_today() 
# to print the day outcome.
import random
def what_happens_today():
    volcano_prob = 0.1
    tsunamis_prob = 0.15
    earthquakes_prob = 0.2
    blizzards_prob = 0.25
    meteors_prob = 0.3
    
    events = ["volcano","tsunamis", "earthquakes", "blizzards", "meteors" ]
    event = random.choice(events)
    return f" Today event will be :{event}"

print(what_happens_today())

#Factorial
def Factorial(num):
    fac_num = 1
    for i in range(num+1):
        if i > 0:
            fac_num *= i
    return fac_num 
print(Factorial(3))