# đỌC NỘI dung tập tin
file = open('Python-18/session-13/demo.txt', 'rt')

print(file)
# đọc lấy  nội dung của file

# lấy vị trí đầu đọc
print(file.tell())


# content = file.read() # đọc tất cả nội dung
content = file.read(5) # lấy 5 kí tự đầu tiên
# in ra nội dung vừa đọc được
print(file.tell())

print(content)