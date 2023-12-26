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
