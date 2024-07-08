my_name = 'Nhân'
my_age = 36

# Tôi tên là my_name, năm nay tôi my_age  tuổi
format_str = "Tôi tên là {0}, năm nay tôi {1} tuổi"

#print(format_str.format(my_name, my_age))

quantity = 2
price = 47.95

txt = "Mua {0} cái bánh hết {1} đô la. Em tôi ăn hết {0} cái bánh"
print(txt.format(quantity, price))

# Cách này áp dụng nhiều nhất
# Rất tường minh
price = 59
# txt_old = "The price is {} dollar"
# print(txt_old.format(price))
txt = f"The price is {price} dollars"
print(txt)

# xin "Chao"

print("xin \"Chao\"") 

# I'm not sure
print('I\'m not sure')

# Day la ki tu \
print('\\')   

