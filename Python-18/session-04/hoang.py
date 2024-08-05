# 1,3,5,7,9
#range(start, stop, step)
for n in range(1, 11):
    # chỉ muốn in ra số chẵn: 2,4,6,8.10
    if n % 2 != 0:
        print(n)