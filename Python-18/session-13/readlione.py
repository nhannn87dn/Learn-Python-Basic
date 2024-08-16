# Muốn đọc đc nội dung
# b1. Mở file
file = open('Python-18/session-13/demo.txt')

# Đọc từng dòng
# line_one = file.readline()
# line_two = file.readline()
# print('line_one', line_one)
# print('line_two', line_two)

# Đọc nhiều dòng và trả về 1 list các dòng đọc đc
multi_line = file.readlines()
print(multi_line)
