n=int(input('Nhập vào n: '))
print(n)
myList =[]
d = range(1,n + 1)
print(d)
for i in d:
    myList.append(i)
print('myList', myList)

# in ra số chẵn trong list
for j in myList:
    if j%2==0:
        print(j, end=' ')
# in ra và bỏ qua phần giá tri 2
for k in myList:
    if k == 2:
        continue # break
    print(k, end=' ')