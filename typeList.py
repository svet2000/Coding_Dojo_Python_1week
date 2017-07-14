list_1 = ['magical unicorns',19,'hello',98.98,'world']
new_string=""
sum=0
if len(new_string)>0 and sum!=0:
    print "This is a mixed string"
elif (new_string)==0 and sum!=0:
    print "This is array with integers"
else:
    print "This is array with strings"
for item in list_1:
        if type(item)==str:
            new_string+=(" "+item)
        if type(item)==int or type(item)==float:
            sum+=item
print "String:",new_string
print "Sum:",sum




# print sum
# "The array you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
