try:
  num = input("num: ")
  print(int(num))
except ValueError:
  print("Vui lòng nhập vào giá trị số")
except:
  print("Lỗi không xác định")