string = "It's thanksgiving day. It's my birthday,too!"
print string
print string.find('day')
print string.replace ('day','aligator')

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
y = [x[0],x[len(x)-1]]
print y

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x.sort()
print x
first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
x[0] = first_list
print x
