# thisset = {"apple", 3.14 , (1, 2), True, False, 30}
# print(type(thisset))

thisset = {"apple", "banana", "cherry"}
# Làm sao để thêm kiwi vào set trên



# Làm sao để in ra  apple
# for i in thisset:
#     if i == 'apple':
#         print(i)
        
# convert qua tupple
# t = tuple(thisset)
# print(type(t), t[0])

## BÀI TẬP
# Câu 1:
# Cho một set  s = {5, 2}
# - In ra phần tử có giá trị là 5
# - Kiểm tra xem 2 có tồn tại trong set trên không
# - Thêm phần tử số 3 vào set trên
# - In ra tổng của các phần tử trong set

s = {5,2}
# yc 1
for i in s:
    if i == 5:
        print(i)
# yc 2
if 2 in s:
    print('2 co ton tai')
else:
    print('2 ko ton tai')
    
# yc3
s.add(3)
print('s ', s)

#yc 4
total = 0
for v in s:
    total += v # cộng dồn trong vòng lặp
print('total', total)