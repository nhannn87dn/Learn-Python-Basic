# 1. Định nghĩa 1 tuple: gồm các chữ số từ 1,2,3,4,5
# 2. In ra phần tử số 3
# 3. Tách và in ra một tuple chứa phần tử 3 và 4
# 4. Thay đổi phần tử số 5 thành 9
# 5. in ra giá trị của từng phần tử trong tuple
my_tuple = (1,2,3,4,5)
print(my_tuple[2])
# my_tuple[start:end]
print(my_tuple[2:4])
#
my_list = list(my_tuple)
my_list[4] = 9
my_tuple = tuple(my_list)
print(my_tuple)