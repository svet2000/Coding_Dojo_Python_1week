#LISTS
fruits=['apple','banana','orange']
veggies=['cucumbers','lettuce']
frAndVeg=fruits+veggies
print frAndVeg
salad=3*veggies
print salad
print fruits[0]

veggies.append('carrot')#built-in method
print veggies
veggies.pop(1)#built-in method
print veggies

print fruits[:]#print the whole list
print fruits[1:]#print the list started from [2]
print fruits[:1]
print fruits[1:2]

print len(fruits)#built-in function

for element in fruits:
    print element

for ind in range(0,3):
    print "Hi"

x = [5,34,10,1,6]
if not x:#if the variable doesn't contain anything
    print 'no'

#DICTIONARIES
capitals={
'Rus':'Moscow',
'Brit':'Lomdon',
'USA':'New York'
}
capitals['CA']='Toronto'
capitals['Fr']='Paris'
print capitals

print capitals['USA']

for data in capitals:
    print data#USA

for key,data in capitals.iteritems():
    print key,data#CA Toronto

for key in capitals.iterkeys():
    print key#USA
print len(capitals)#built-in functions
print type(capitals)

print capitals.copy()#built-in methods -returns a dictionary
print capitals.items()#returns a list of tuples
print capitals.keys()#returns ['Rus', 'CA', 'Fr', 'USA', 'Brit']
print capitals.values()#returns ['Moscow', 'Toronto', 'Paris', 'New York', 'Lomdon']

#NESTED DICTIONARIES
context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }
for key,data in context.items():#nested loop
     #print data
     for value in data:
         print value['id'],':',value['content']

#LIST FROM DICTIONARIES
data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()#returns [('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()#returns ['house', 'red', 'cat']
print data.values()#returns ['Haus', 'rot', 'Katze']

#DICTIONARIES FROM LISTS
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
countries_dishes = zip(countries, dishes)
print countries_dishes #returns [('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
countries_dishes_dict = dict(countries_dishes)
print countries_dishes_dict#returns {'Germany': 'sauerkraut', 'Italy': 'pizza', 'USA': 'hamburger', 'Spain': 'paella'}
