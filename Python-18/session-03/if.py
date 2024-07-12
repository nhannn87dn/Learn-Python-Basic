# Nếu trời tạnh mưa thì tôi sẽ được đi chơi

# if trời tạnh mưa:
#     đi chơi

# x = 5
# if x > 0: # True
#     print('yes')
#     print('yes')
#     print('yes')
#     print('yes')
    
# level = 'VIP'
# totalOrder = 4000
# if level == 'SILVER' and totalOrder > 2000:
#     print('được giảm 5%')

# hung = 'green'

# if hung == 'yellow':
#     print('len bang')
# else:
#     print('ko len bang')


'''
Nếu dtb >= 9 thì in ra Xuất sắc
Nếu dtb >= 8 thì in ra Giỏi
Nếu dtb >= 6 và < 8 thì in ra Khá
Nếu dtb > 4.5 và < 6 thì in ra Trung Bình
Còn lại là in ra là Yếu
'''
dtb_ngoc = 7.50
if dtb_ngoc >= 9:
    print('Xuất sắc')
elif dtb_ngoc >= 8 and dtb_ngoc < 9:
    print('Giỏi')
elif dtb_ngoc >= 6 and dtb_ngoc < 8:
    print('Khá')
elif dtb_ngoc >= 4.5 and dtb_ngoc < 6:
    print('Trung Bình')
else:
    print('Yếu')