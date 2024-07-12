# Tạo mới một file .txt, với mode = x
'''
Tham số đầu tiên là đường dẫn nơi file cần tạo
'''
file = open("Python-17/Session-08/new_file.txt", "x")
# Ghi nội dung vào trước khi tạo
file.write("noi dung moi")
file.close()
