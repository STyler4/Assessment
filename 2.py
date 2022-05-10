# ----- Create a list with no repeating elements ------ #

mylist = [67, 7, 89, 7, 2, 7]
newlist = []

for i in mylist:
    if i not in newlist:
        newlist.append(i)
