# def draw_stars(x):
#     for item in x:
#         print item*"*"
# arr=[2,6,3,5,9,8,3]
# draw_stars(arr)

def draw_stars1(x):
    for item in x:
        if type(item)==str:
            print (item[0].lower())*len(item)
        if type(item)==int:
            print item*'*'
a=[4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars1(a)
