# 1. Định nghĩa một từ điển mô tả các trường thông tin của bản thân:
#     tên, tuổi, số đt, email,  địa chỉ,  trường học...
    
# 2. In ra giá trị của một trường thông tin bất kỳ ở trên.

# 3. Thêm mới trường color vào từ điển trên

# 4. Sử dụng vòng lặp for để in ra từng giá trị của các phần tử trong 
# tử điển nêu trên.

intro = {
    "name": "An",
    "age": 12,
    "mobile": "0988777666",
    "email": "an@example.com"
}

# 2
print(intro['name'])
# 3
intro['color'] = 'pink'
print(intro)
# 4

# for k in intro:
#     print(intro[k])

# for v in intro.values():
#     print(v)

