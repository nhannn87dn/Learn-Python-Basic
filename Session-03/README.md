# Buổi 3: Luồng điều khiển và Vòng lặp

## I. Câu lệnh điều kiện

Trong Python, chúng ta sử dụng câu lệnh `if`, `else`, và `elif` để thực hiện điều khiển dựa trên một hoặc nhiều điều kiện.

1. Câu lệnh `if`:

```python
if điều_kiện:
    # Mã được thực thi nếu điều_kiện là True
```

2. Câu lệnh `else`:

```python
if điều_kiện:
    # Mã được thực thi nếu điều_kiện là True
else:
    # Mã được thực thi nếu điều_kiện là False
```

3. Câu lệnh `elif`:

```python
if điều_kiện_1:
    # Mã được thực thi nếu điều_kiện_1 là True
elif điều_kiện_2:
    # Mã được thực thi nếu điều_kiện_2 là True
else:
    # Mã được thực thi nếu không có điều_kiện nào đúng
```

### II. Cấu trúc lặp

Python cung cấp hai cấu trúc lặp chính là vòng lặp `while` và `for` để thực hiện một nhóm câu lệnh nhiều lần.

1. Vòng lặp `while`:

```python
while điều_kiện:
    # Mã được lặp lại cho đến khi điều_kiện là False
```

2. Vòng lặp `for`:

```python
for biến in tập_hợp:
    # Mã được lặp lại cho mỗi phần tử trong tập_hợp
```

## III. Câu lệnh `break` và `continue`

Câu lệnh `break` được sử dụng để thoát khỏi vòng lặp hiện tại và tiếp tục thực hiện các câu lệnh sau vòng lặp. Câu lệnh `continue` được sử dụng để bỏ qua phần còn lại của vòng lặp và tiếp tục với lần lặp tiếp theo.

```python
while điều_kiện:
    if điều_kiện_dừng:
        break
    if điề

u_kiện_bỏ_qua:
        continue
    # Mã được lặp lại cho đến khi điều_kiện là False
```

