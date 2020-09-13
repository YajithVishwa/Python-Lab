mylist = [int(x) for x in input().split()]
mylist = list(dict.fromkeys(mylist))
print(mylist)
