# Dạng đầy đủ
x = range(1, 6, 2)
# Start: 1, Stop: 6, Step : 1
# for n in x:
#   print('n',n)
  
# Dạng khuyết: start, step
y = range(6) # PY hiểu 6 chính là Stop
# KL: Chạy từ 0 đến stop -1

# for m in y:
#   print('m',m)
  
# Dạng khuyết: step
# z = range(1,6) # PY hiểu step là 1
# for p in z:
#   print('p',p)
  
# Dạng Đảo hướng lặp, ngược lại: 6--> 1
z = range(6,0,-1) # start: 6, step: 0, step: -1
for p in z:
  print('p',p)