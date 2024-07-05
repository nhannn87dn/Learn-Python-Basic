# x = 1
# y = 2

# if x > y: #true
#     print('x > y')
#     print('đúng')


'''
Nếu a > 0 thì in ra là số dương, còn lại là số 0 hoặc âm
'''
# a = -5
# if a > 0:
#     print('Số dương')
# else:
#     print('Số âm hoặc = 0')

'''
Điểm trung bình cộng môn học: 7.5
- Nếu DTB > 9 thì in ra là xuất sắc
- Nếu DTB >=8 và < 9 in ra là Giỏi
- Nếu DTB >=6.5 và < 8 thì in ra Khá
- Còn lại Trung bình
'''
dtb = 7.5
if(dtb > 9):
    print('Xuất sắc')

if(dtb >= 8 and dtb < 9):
    print('Giỏi')
if(dtb >= 6.5 and dtb < 8):
    print('Khá')
else:
    print('Trung bình')