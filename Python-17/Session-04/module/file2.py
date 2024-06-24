from myModule import multiply
# Chỉ lấy hàm multiply ở trong myModule
import datetime
import random

x =multiply(4,5)
print(x)

current_time = datetime.datetime.now()
print("Thời gian hiện tại:", current_time)

formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")

print("Thời gian hiện tại:", formatted_time)


print(random.randint(1, 10))



