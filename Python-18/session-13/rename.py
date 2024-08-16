import os

fileName = 'Python-18/session-13/ghi.txt'
if os.path.exists(fileName):
    os.rename(fileName, 'Python-18/session-13/write.txt')
else:
    print('File không tồn tại')    