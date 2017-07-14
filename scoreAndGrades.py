import random
def gradesFunc(students):

    for x in range(0,students):
        random_num=random.randint(60,101)
        if random_num>=60 and random_num<=69:
            print "The grade is ",random_num,". Your grade is D."
        if random_num>=70 and random_num<=79:
            print "The grade is ",random_num,". Your grade is C."
        if random_num>=80 and random_num<=89:
            print "The grade is ",random_num,". Your grade is B."
        if random_num>=90 and random_num<=100:
            print "The grade is ",random_num,". Your grade is A."
gradesFunc(10)
