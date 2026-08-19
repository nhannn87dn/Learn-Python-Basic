# myTuple = ('apple', 'apple', True, 2, 1.2, (1,2))

# print(myTuple[2])

# myTuple[1] = 'lemon'

# print(myTuple)

theTuple = ('apple',)
print(type(theTuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")

print(thistuple[1:4])

# thay đổi giá trị phần tử của tuple bằng cách
# bước 1: convert tuple thành list
ls = list(thistuple)
ls[1] = 'lemon'
# bước 2: convert list thành tuple
thistuple = tuple(ls)
print(thistuple)

