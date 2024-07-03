# Định nghĩa
my_tup = ()
my_tup = ('Nhan',)
print(type(my_tup))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
print(thistuple[1])
# Thay đổi giá trị

# b1. Chuyển tupe thành list
convert_tuple_to_list = list(thistuple) # tuple --> list
#b2. can thiệp phần tử của list
convert_tuple_to_list[1] = 'Lemon'
#b3 Chuyển list thành tuple
thistuple = tuple(convert_tuple_to_list)
#b4 kết quả
print(thistuple)

# Truy cập phần tử của Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print('yellow',yellow)


mytuple = ("apple", "banana", "kiwi")
for x in mytuple:
    print(x)
