# Ghi nội dung vào 1 file rỗng đã tồn taại

# b1. Mở  tập tin
#file = open('Python-18/session-13/ghi.txt', 'a') # a ghi nối tiếp cuối file
file = open('Python-18/session-13/ghi.txt', 'w') # ghi đè nội dùng
# b2 ghi nội dung vào file
content = "Xu ly file voi python"
file.write(content)

file.close() # đóng file lại để giải phóng bộ nhớ

