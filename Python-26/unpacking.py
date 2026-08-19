# lấy tất cả
# fruits = ("apple", "banana", "cherry")
# (a, b, c) = fruits
# # lấy 1 phần ví dụ chỉ lấy banana
# (_, ba, _) = fruits
# print(ba)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a, *newFruits) = fruits
print(a)
print(newFruits)
