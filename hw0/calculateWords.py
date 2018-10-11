content = open("words.txt").read()
array = content.split(' ')

orderindex = 0
for i in range(array.__len__()):
    if array.index(array[i]) == i:
        print("%s %s %s" % (array[i], orderindex, array.count(array[i])))
        orderindex += 1
