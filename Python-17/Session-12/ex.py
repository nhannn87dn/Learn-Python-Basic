try:
    # Cố gắng mở file để chuẩn bị đọc
    file = open("file.txt", "rt")
except FileNotFoundError:
    print("File không tồn tại")
else:
    # In ra nội dung nếu file tồn tại
    print(file.read())
finally:
    print("Kết thúc đọc file")
# Câu lệnh chương trình tiếp theo  
print("next Step")