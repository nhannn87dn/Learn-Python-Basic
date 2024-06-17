# x = 5
# y = 2

'''
# Ngôn ngữ nói
Nếu x > y thì in ra là Đúng
'''
# ngôn ngữ lập trình
# if x > y:
#     print('Đúng')
    
'''
# Ngôn ngữ nói
Nếu x > y thì in ra là Đúng
Còn không thì in ra Sai
'''
# x = 5
# y = 2

# if x < y:
#     print('Đúng')
# else:
#     print('Sai')
    

'''
Nếu là thành viên VIP    --> thì được giảm 10%
Nếu là thành viên GOLD --> thì được giảm 7%
Nếu là thành viên SILVER   --> thì được giảm 5%
Còn lại thì không giảm
'''
level = 'SILVER' # hạng thành viên
totalOrder = 2000 # Tổng giá trị đơn hàng

if level == 'VIP' and totalOrder >= 5000:
    print('10%')
elif level == 'GOLD' and totalOrder >= 5000:
    print('7%')
elif level == 'SILVER'  and totalOrder >= 5000:
    print('5%')
else:
    print('0%')
    
