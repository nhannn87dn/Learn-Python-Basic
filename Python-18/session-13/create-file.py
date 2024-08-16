# tạo mới file với mode x, create
try:
    file = open('Python-18/session-13/taomoi.txt', 'x')
    file.close() # giải phóng bộ nhớ
except FileExistsError:
    print('File đã tồn tại')
except:
    print('Có lỗi xảy ra')
