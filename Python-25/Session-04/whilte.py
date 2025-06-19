# count = 0
# while count < 5:
#     if(count == 2):
#         break # bỏ qua câu lệnh phía sau nó, thoát khỏi vòng lặp
#     print(count)
#     count += 1

# for x in range(1,5):
#     if x == 2:
#         continue # tv = tiếp tục==> bỏ qua câu lệnh phía sau và tiếp tục vòng lặp
#     print(x)

# Câu 1: Cho một dãy số với start = 1, stop = 10
# hãy in ra ra các số từ 1 - 5;

# Câu 1: Cho một dãy số với start = 1, stop = 8
# hãy in ra ra các số  2 - 4 - 6 .Nhưng ko dùng toán tử %;
for i in range(1,8):
    if i == 1 or i == 3 or i == 5 or i == 7:
        continue# bỏ qua câu lệnh phía sau, và tiếp tục vòng lặp
    print(i)