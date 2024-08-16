import os

fileName = 'Python-18/session-13/taomoi.txt'
if os.path.exists(fileName):
    os.remove(fileName)
else:
    print('File không tồn tại')