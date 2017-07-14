# Build a function that takes in a list of numbers and a value. Multiply each number in the list by the value given and return the updated list. Example: given [1,2,3], 5 return [5,10,15]
def multifunc(list_1,num):
    for ind in range(0,len(list_1)):
        list_1[ind]=list_1[ind]*num
    return list_1
print multifunc([1,2,3],5)

# Build a function that takes in a dictionary. Print the key and value of each key-value pair like so:
# Your dictionary has the following inside:# key1 : value1
def dictfunc(dict):
    for key in dict:
        print key,":",dict[key]
dictfunc({'first_name':'Svetlana', 'last_name':'Stepanyan'})

# Create a function that will examine the range of numbers from 1 to 100. If a number is divisible by 3, print "fizz", if a number is divisible by 5, print "buzz", if a number is divisible by 3 and 5, print "fizzbuzz"
def numberfunc():
    for num in range(1,101):
        if num%3==0 and not num%5==0:
            print "fizz"
        elif num%5==0 and not num%3==0:
            print "buzz"
        if num%3==0 and num%5==0:
            print "fizzbuzz"

numberfunc()
 
