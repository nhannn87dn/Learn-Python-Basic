# 1. Định nghĩa 1 list: gồm các chữ số từ 1,2,3,4,5
# 2. In ra phần tử số 3
# 3. Tách và in ra một list chứa phần tử 3 và 4
# 4. Thay đổi phần tử số 5 thành 9
# 5. in ra giá trị của từng phần tử trong list
numbers = [1,2,3,4,5]
#2
print(numbers[2])
# 3
print(numbers[2:4])
# 4
numbers[4] = 9
# 5
for n in numbers:
    print(n)