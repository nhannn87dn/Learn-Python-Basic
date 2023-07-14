# Session 01 - Giới thiệu về Python

## 1. Tổng quan về Python (15 phút)

### 1.1 Giới thiệu về Python và lịch sử phát triển

- Python là ngôn ngữ lập trình thông dịch, mạnh mẽ và dễ học được tạo ra bởi Guido van Rossum vào năm 1989.
- Python được thiết kế với nguyên tắc đơn giản, dễ đọc và dễ hiểu, nhằm tăng tính khả đọc và khả bảo trì của mã nguồn.
- Python là ngôn ngữ mã nguồn mở, có cộng đồng lớn và hỗ trợ đa nền tảng, giúp phát triển ứng dụng trên nhiều hệ điều hành khác nhau.

### 1.2 Ưu điểm và ứng dụng của Python

- Python có cú pháp đơn giản, gần gũi với ngôn ngữ tự nhiên, dễ học và dễ sử dụng.
- Python hỗ trợ nhiều thư viện và module mạnh mẽ, giúp giải quyết các tác vụ phức tạp một cách hiệu quả.
- Python là một ngôn ngữ đa năng, được sử dụng rộng rãi trong nhiều lĩnh vực như phân tích dữ liệu, trí tuệ nhân tạo, lập trình web, thiết kế giao diện, và nhiều hơn nữa.
- Python có cộng đồng lớn và phong phú, hỗ trợ người dùng thông qua tài liệu, diễn đàn và thư viện mã nguồn mở.

### 1.3 So sánh Python với các ngôn ngữ lập trình khác

1.3 So sánh Python với các ngôn ngữ lập trình khác

Python là một ngôn ngữ lập trình mạnh mẽ và linh hoạt, được so sánh và sử dụng rộng rãi trong nhiều lĩnh vực khác nhau. Dưới đây là một số so sánh giữa Python và các ngôn ngữ lập trình khác như C, Java và JavaScript:

1.3.1 So sánh Python với C:
- Ưu điểm của Python so với C:
  - Cú pháp đơn giản và dễ hiểu hơn.
  - Hỗ trợ tự động quản lý bộ nhớ, giúp tránh các lỗi gây ra bởi việc quản lý bộ nhớ thủ công trong C.
  - Có nhiều thư viện mạnh mẽ và module bên thứ ba, giúp phát triển nhanh chóng và tiết kiệm thời gian.
- Nhược điểm của Python so với C:
  - Tốc độ thực thi chậm hơn do quá trình phiên dịch và kiểm tra kiểu dữ liệu.
  - Không phù hợp cho các ứng dụng yêu cầu hiệu năng cao hoặc lập trình nhúng.

1.3.2 So sánh Python với Java:
- Ưu điểm của Python so với Java:
  - Cú pháp đơn giản và dễ hiểu hơn, giúp giảm thời gian và công sức phát triển.
  - Có sẵn một loạt các thư viện và framework mạnh mẽ, giúp phát triển ứng dụng nhanh chóng.
  - Tính di động cao, có thể chạy trên nhiều hệ điều hành khác nhau.
- Nhược điểm của Python so với Java:
  - Tốc độ thực thi chậm hơn và tài nguyên tiêu tốn cao hơn.
  - Kiểm soát kiểu dữ liệu không nghiêm ngặt như trong Java.

1.3.3 So sánh Python với JavaScript:

- Ưu điểm của Python so với JavaScript:
  - Cú pháp đơn giản và dễ hiểu hơn, giúp giảm thời gian và công sức phát triển.
  - Có thể sử dụng cả phía máy chủ và phía khách hàng, đồng thời giúp tạo ra các ứng dụng web đa nền tảng.
  - Có nhiều thư viện và framework mạnh mẽ, giúp phát triển ứng dụng web dễ dàng.
- Nhược điểm của Python so với JavaScript:
  - Tốc độ thực thi chậm hơn trong một số trường h

ợp.
  - Không thể chạy trực tiếp trên trình duyệt, cần có trình thông dịch hoặc máy ảo để chạy mã Python trên phía khách hàng.

Các dự án và ứng dụng nổi tiếng được xây dựng bằng Python:
- Django: Framework phát triển ứng dụng web mạnh mẽ và linh hoạt.
- Flask: Framework nhẹ và dễ sử dụng cho phát triển ứng dụng web.
- NumPy và SciPy: Thư viện tính toán khoa học và xử lý dữ liệu mạnh mẽ.
- Pandas: Thư viện phân tích và xử lý dữ liệu.
- TensorFlow và PyTorch: Frameworks học máy và trí tuệ nhân tạo.
- YouTube, Instagram, Dropbox: Các ứng dụng nổi tiếng đã sử dụng Python trong quá trình phát triển.


---

## 2. Cài đặt Python và thiết lập môi trường phát triển (30 phút)

### 2.1 Giới thiệu về các phiên bản Python

- Giới thiệu về các phiên bản Python phổ biến như Python 2.x và Python 3.x.
- Giải thích sự khác biệt giữa các phiên bản và lựa chọn phiên bản phù hợp.

### 2.2 Hướng dẫn cài đặt Python trên hệ điều hành Windows

1. Truy cập trang web chính thức của Python (https://www.python.org) và tải xuống bản cài đặt phù hợp với hệ điều hành Windows.
2. Chạy tệp tin cài đặt và tuân theo các bước hướng dẫn để hoàn tất quá trình cài đặt Python.
3. Kiểm tra cài đặt bằng cách mở cửa sổ Command Prompt và chạy lệnh `python --version`.

### 2.3 Hướng dẫn cài đặt Python trên hệ điều hành macOS

1. Mở Terminal trên máy tính Mac.
2. Sử dụng Homebrew để cài đặt Python bằng cách chạy lệnh `brew install python`.
3. Kiểm tra cài đặt bằng cách chạy lệnh `python3 --version`.

### 2.4 Hướng dẫn cài đặt Python trên hệ điều hành Linux

1. Mở Terminal trên máy tính Linux.
2. Sử dụng trình quản lý gói của hệ điều hành để cài đặt Python, ví dụ như `apt` cho Ubuntu hoặc `yum` cho CentOS.
3. Kiểm tra cài đặt bằng cách chạy lệnh `python3 --version`.

### 2.5 Cài đặt trình biên dịch và trình chỉnh sửa code

- Giới thiệu về trình biên dịch (interpreter) và trình chỉnh sửa code phổ biến như Visual Studio Code, PyCharm, Sublime Text.
- Hướng dẫn cài đặt một trong những trình chỉnh sửa code trên máy tính của sinh viên.

### 2.6 Thiết lập môi trường ảo (virtual environment)

- Giới thiệu về môi trường ảo và lợi ích của việc sử dụng môi trường ảo trong phát triển Python.
- Hướng dẫn cài đặt và sử dụng công cụ `virtualenv` để tạo môi trường ảo.



---


## 3. Chạy chương trình Python đầu tiên (15 phút)

### 3.1 Giới thiệu Extension Python cho VSCode

- Cài đặt Extension Python cho VSCode
- Extension Python - một công cụ cho phép thực thi mã nguồn Python.

### 3.2 Viết và chạy chương trình Python đơn giản

1. Mở IDLE hoặc trình chỉnh sửa code được cài đặt trước đó.
2. Tạo một tệp tin mới và lưu nó với phần mở rộng `.py` (ví dụ: `hello.py`).
3. Viết chương trình Python đơn giản để in ra màn hình dòng chữ "Hello, Python!".
4. Lưu tệp tin và chạy chương trình bằng cách nhấn phím F5 hoặc chọn "Run" từ menu.

### 3.3 Giải thích cú pháp cơ bản của Python

- Giới thiệu cú pháp cơ bản của Python như khai báo biến, in ra màn hình, điều khiển luồng, vòng lặp và hàm.
- Cung cấp ví dụ minh họa và giải thích cách sử dụng cú pháp trong các trường hợp cụ thể.

### 3.4 Tài liệu tham khảo và tài nguyên học tập

- Giới thiệu các tài liệu tham khảo và tài nguyên học tập về Python như tài liệu trực tuyến, sách và khóa học trực tuyến.
- Chính thống: <https://docs.python.org/3/tutorial/index.html>

- W3School: <https://www.w3schools.com/python/python_intro.asp>

## IV. Bài tập và thảo luận (15 phút)

- Yêu cầu sinh viên thực hành viết và chạy chương trình Python đơn giản.
- Thảo luận và giải đáp các câu hỏi liên quan đến giới thiệu về Python và quá trình cài đặt.

## V. Tổng kết và đánh giá (5 phút)

- Tóm tắt lại nội dung đã học trong buổi.
- Nhắc lại các lợi ích của việc học Python và môi trường phát triển.
- Thực hiện đánh giá sự hiểu biết của sinh viên qua câu hỏi hoặc bài kiểm tra nhỏ.

## VI. Hướng dẫn cho Buổi 2 (5 phút)

- Giới thiệu chủ đề và nội dung của buổi 2.
- Nhắc lại các yêu cầu chuẩn bị trước buổi học tới.
