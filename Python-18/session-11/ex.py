# 1. Định nghĩa 1 set gồm 5 kiểu dữ liệu khác nhau
# 2. In ra các phần tử của set nói trên
# 3. Kiểm tra xem phần tử "one" đã tồn tại trong set chưa?
# 4. Thêm phần tử "one" vào set nếu chưa có

# try:
#     # Nếu thành công thì thì code trong này chạy
#     my_set = { [1,2]}
#     print(my_set)
# except:
#     # nếu lỗi nó sẽ rơi vào phần except
#     print('Kiểu set không chấp nhận kiểu dữ liệu LIST')
    


# import random
 
# try:
#     r = random.randint(1,3) # lấy giá trị ngẫu nhiên cho r
#     if r == 1:
#         print(int("Fred")) # chuyển thành số nguyên sai
#     elif r == 3:
#         [][2] = 5 # giá giá trị cho index không tồn tại
#     # Phép chia một số cho 0
#     print(3/0)
    
# except ValueError:
#     print("Không thể chuyển thành số nguyên")
# except IndexError:
#     print("Chỉ số không tồn tại")
# except ZeroDivisionError:
#     print("Không thể chia cho 0")

'''
Yêu cầu nhập vào một số nguyên.
Kiểm tra:
- Nếu số đó > 0 thì in ra là số Dương
- Nếu < 0 thì in ra là số âm
- Còn lại là là số 0
'''
# try:
#     num = int(input('Nhập vào một số nguyên: '))
#     print(num, type(num))
#     if num > 0:
#         print('Số Dương')
#     elif num < 0:
#         print('Số âm')
#     else:
#         print('Số 0')
# except ValueError:
#     print('Bạn phải nhập vào một số nguyên')
# except: # Bất kỳ lỗi thuộc loại gì nó đều rơi vào except
#     print('Lỗi không xác định')

# try:
#     result =  5 / 0
# except ZeroDivisionError:
#     print('Không thể chia cho 0')
# else: # nó chạy khi ko có bất kỳ lỗi gì
#     print('result', result)
# finally: # dù lỗi hay ko lỗi thì nó vẫn chạy
#     print('Chương trình chạy xong !')
    
    
try:
    result =  5 / 2
    print('result', result)
except ZeroDivisionError:
    print('Không thể chia cho 0')
finally: # dù lỗi hay ko lỗi thì nó vẫn chạy
    print('Chương trình chạy xong !')