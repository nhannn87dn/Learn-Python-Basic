# Buổi 4 -  Range và Vòng lặp

## Câu lệnh `range()`


## Vòng lặp trong Python

### Vòng lặp `for`

Vòng lặp `for` được sử dụng để lặp qua một dãy (list, tuple, dictionary, set, hoặc string).

#### Cấu trúc Vòng lặp `for`

```python
for variable in iterable:
    # code to execute on each iteration
```

#### Ví dụ

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Vòng lặp `while`

Vòng lặp `while` được sử dụng để lặp lại một khối mã miễn là điều kiện cho trước là `True`.

#### Cấu trúc Vòng lặp `while`

```python
while condition:
    # code to execute on each iteration
```

#### Ví dụ

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### Sử dụng `break` và `continue` trong vòng lặp

`break`: Dừng vòng lặp ngay lập tức.
`continue`: Bỏ qua phần còn lại của khối mã trong vòng lặp và tiếp tục với lần lặp kế tiếp.


```python
while điều_kiện:
    if điều_kiện_dừng:
        break
    if điều_kiện_bỏ_qua:
        continue
    # Mã được lặp lại cho đến khi điều_kiện là False
```

Ví dụ:

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```
