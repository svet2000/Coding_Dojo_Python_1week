def oddEvenFunc():
    for item in range(1,2001):
        if item%2==0:
            print "The number is ",item,". This is an even number."
        if item%2==1:
            print "The number is ",item,". This is an odd number."
oddEvenFunc()

def multiFunc(list,a):
    for ind in range(0,len(list)):
        list[ind]*=a
        return list
print multiFunc([1,2,3,4],5)

def layered_multiples(arr):
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Copy
