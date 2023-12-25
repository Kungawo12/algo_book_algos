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