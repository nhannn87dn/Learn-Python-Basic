# myTuple= ('1', 1, 1, True, False, (1,2,3))
# print(type(myTuple))

# print(myTuple[1:3])

x = ("apple", "banana", "cherry")
## bước 1 biến tuple thành list
l = list(x)
print(type(l), l)
# Bước 2 thay đối giá trị
l[1] = 'Kiwi'
print( l)
# Bước 3 convert list thành tuple lại
x = tuple(l)
print(x)


#
fruits = ("apple", "banana", "cherry")
(_, _, c) = fruits
print(c)

