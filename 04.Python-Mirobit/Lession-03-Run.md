# Run - Điều khiển động cơ

Hiện tại Microbit Python Editor chưa hỗ trợ Module dể điều khiển bộ kít xe robot xe Zoombit

## 🔥 Động cơ Motor DC

Bộ kit zoom:bit được trang bị 2 động cơ giảm tốc để di chuyển.

![mt](img/dc-motor.png)


## 🔥 Động cơ Servo

Servo Motor là phần động cơ được gắn dưới đầu xe robot zoom:bit. Bạn có thể xoay đầu 180 độ với động cơ này.

![sv](img/servor.png)

## 🔥 Đèn Trước

![rgb](img/rgb-led.png)



## 🔥 Đèn RGB LED Trên bo mạch REKA:bit


## 🔥 Điều khiển qua sóng Radio


## 💛 THỰC HÀNH

### 🔥 Task 1 - Xe cảnh sát zoom:bit

Sử dụng zoom:bit giả làm một xe cảnh sát với yêu cầu chương trình như sau:

- Khởi động lên:
  - thì cho Servo xoay đầu phía trước
  - Màn hình LED hiển thị mặt cười. Bật âm thanh power up
  - Đèn trước tự động sáng khi trời tối
- Nhấn button A:
  -  đầu xoay phải,
  - màn hình LED hiển thị mũi trên hướng phải
- Nhấn button B:
  - đầu xoay trái 
  - màn hình LED hiển thị mũi trên hướng trái
- Nhấn button A+B:
  - đầu xoay ra trước
  - màn hình LED hiển thị mũi trên hướng lên
- Chạm Logo:
  -  đầu xoay ra trước
  - màn hình LED hiển thị mũi trên hướng xuống

Ngoài ra:

Để tăng sự thu hút của mọi người
và nhường đường để xe chạy, bạn
có thể vừa cho đèn RGB LED nhấp
nháy liên tục 2 màu Xanh Đỏ vừa
phát ra tiếng còi báo động bằng các
khối âm thanh


### 🔥 Task 2 - Điều khiển xe với Radio

Cũng với cách lập trình trên, nhưng sử dụng 2 micobit
- 1 Cái gửi tín hiệu 
  - Nhấn A, thì gửi đi chữ `right`
  - Nhấn B, thì gửi đi chữ `left`
  - Nhấn A+B, thì gửi đi chữ `backward`
  - Nhấn Logo, thì gửi đi chữ `forward`
- 1 Cái nhận tín hiệu
  - Khi nhận được chữ `right`:
    -  đầu xoay phải,
    - màn hình LED hiển thị mũi trên hướng phải
  - Nhấn B, thì gửi đi chữ `left`
    - đầu xoay trái 
    - màn hình LED hiển thị mũi trên hướng trái
  - Nhấn A+B, thì gửi đi chữ `backward`
    - đầu xoay ra trước
    - màn hình LED hiển thị mũi trên hướng lên
  - Nhấn Logo, thì gửi đi chữ `forward`
    -  đầu xoay ra trước
    - màn hình LED hiển thị mũi trên hướng xuống