# OOP Python

## OOP là gì

**OOP (Object-Oriented Programming)**, hay lập trình hướng đối tượng, là một mô hình lập trình tổ chức phần mềm xung quanh các đối tượng, thay vì các hành động và logic. Các đối tượng có thể được xem như các thực thể trong thế giới thực có các thuộc tính (properties) và hành vi (methods).

### Các khái niệm cơ bản của OOP

1. **Lớp (Class)**:
    - Lớp là một mẫu (blueprint) để tạo ra các đối tượng. Nó định nghĩa các thuộc tính và phương thức mà các đối tượng thuộc lớp đó sẽ có.
    - Ví dụ: Một lớp `Car` có thể có các thuộc tính như `color`, `model` và các phương thức như `drive()`, `stop()`.

    ```python
    class Car:
        def __init__(self, model, color):
            self.model = model
            self.color = color

        def drive(self):
            print(f"{self.model} is driving")

        def stop(self):
            print(f"{self.model} has stopped")
    ```

2. **Đối tượng (Object)**:
    - Đối tượng là một thể hiện cụ thể của một lớp. Khi một lớp được định nghĩa, không có bộ nhớ nào được cấp phát cho đến khi một đối tượng của lớp đó được tạo ra.
    - Ví dụ: `my_car = Car("Toyota", "Red")` tạo ra một đối tượng của lớp `Car`.

    ```python
    my_car = Car("Toyota", "Red")
    my_car.drive()  # Output: Toyota is driving
    ```

3. **Tính kế thừa (Inheritance)**:
    - Tính kế thừa cho phép một lớp con kế thừa các thuộc tính và phương thức từ một lớp cha.
    - Ví dụ: `ElectricCar` kế thừa từ `Car` và thêm các thuộc tính hoặc phương thức mới.

    ```python
    class ElectricCar(Car):
        def __init__(self, model, color, battery_capacity):
            super().__init__(model, color)
            self.battery_capacity = battery_capacity

        def charge(self):
            print(f"{self.model} is charging")
    ```

4. **Tính đa hình (Polymorphism)**:
    - Tính đa hình cho phép các đối tượng thuộc các lớp khác nhau có thể được xử lý thông qua cùng một giao diện.
    - Ví dụ: Các lớp `Dog` và `Cat` đều có phương thức `make_sound`, và chúng ta có thể gọi phương thức này mà không cần biết đối tượng thuộc lớp nào.

    ```python
    class Dog:
        def make_sound(self):
            return "Woof!"

    class Cat:
        def make_sound(self):
            return "Meow!"

    def animal_sound(animal):
        print(animal.make_sound())

    dog = Dog()
    cat = Cat()
    animal_sound(dog)  # Output: Woof!
    animal_sound(cat)  # Output: Meow!
    ```

5. **Tính đóng gói (Encapsulation)**:
    - Tính đóng gói liên quan đến việc ẩn các chi tiết triển khai của một lớp và chỉ hiển thị các giao diện công khai (public interface).
    - Ví dụ: Các thuộc tính của một lớp có thể được làm riêng tư (private) và được truy cập thông qua các phương thức công khai.

    ```python
    class BankAccount:
        def __init__(self, owner, balance):
            self.__owner = owner
            self.__balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount

        def get_balance(self):
            return self.__balance

    account = BankAccount("Alice", 1000)
    account.deposit(500)
    print(account.get_balance())  # Output: 1500
    ```

### Lợi ích của OOP

- **Tái sử dụng mã (Code Reusability)**: Các lớp có thể được tái sử dụng trong các phần khác của chương trình hoặc trong các dự án khác nhau.
- **Dễ bảo trì (Maintainability)**: Mã nguồn dễ dàng bảo trì và nâng cấp do tính mô-đun hóa.
- **Mô hình hóa thế giới thực (Real-World Modeling)**: OOP cho phép mô hình hóa các thực thể trong thế giới thực một cách tự nhiên và trực quan.
- **Tăng cường bảo mật (Enhanced Security)**: Tính đóng gói giúp bảo vệ dữ liệu và logic bên trong các đối tượng.

OOP là một trong những mô hình lập trình phổ biến và mạnh mẽ nhất, được sử dụng rộng rãi trong phát triển phần mềm hiện đại.

## Class là gì


Trong lập trình hướng đối tượng (OOP), **class** (lớp) là một bản mẫu (blueprint) dùng để tạo ra các đối tượng (objects). Lớp định nghĩa các thuộc tính (properties) và phương thức (methods) mà đối tượng thuộc lớp đó sẽ có. Bạn có thể xem lớp như một khuôn mẫu hoặc bản thiết kế cho các đối tượng.

### Định nghĩa 1 Class

```python
class Car:
    pass
```

- Sử dụng từ khóa `class` để định nghĩa 1 class
- Tên của Class phải bắt đầu bằng một ký tự HOA, kết thức bằng dấu:


### Thành phần của một Class

1. **Thuộc tính (Attributes)**:
    - Thuộc tính là các biến lưu trữ dữ liệu của đối tượng. Chúng thường được gọi là biến thực thể (instance variables).
    - Ví dụ: Một lớp `Car` có thể có các thuộc tính như `color`, `model`.

    ```python
    class Car:
        color = 'Black'
        model = 2022
    ```

2. **Phương thức (Methods)**:
    - Phương thức là các hàm định nghĩa các hành vi của đối tượng. Chúng thường thao tác trên các thuộc tính của đối tượng.
    - Ví dụ: Một lớp `Car` có thể có các phương thức như `drive()`, `stop()`.

    ```python
    class Car:
        color = 'Black'
        model = 'Toyota'

        # Phương thức để mô phỏng hành vi lái xe
        def drive(self):
            print(f"{self.model} is driving")

        # Phương thức để mô phỏng hành vi dừng xe
        def stop(self):
            print(f"{self.model} has stopped")
    ```

    - `self` là tham số đầu tiên trong tất cả các phương thức của lớp. Nó là tham chiếu đến đối tượng hiện tại của lớp và được sử dụng để truy cập các thuộc tính và phương thức của lớp.

### Tạo đối tượng từ Class

Sau khi định nghĩa lớp, bạn có thể tạo ra các đối tượng từ lớp đó. Dưới đây là cách tạo một đối tượng `Car` và gọi các phương thức của nó:

```python
# Tạo đối tượng từ lớp Car
my_car = Car()

# Truy cập các thuộc tính của lớp Car
print(my_car.color) ## Output: Black
print(my_car.model) ## Output: Toyota

# Gọi các phương thức của đối tượng
my_car.drive()  # Output: Toyota is driving
my_car.stop()   # Output: Toyota has stopped
```

### Phương thức khởi tạo __init__

Phương thức khởi tạo `__init__` trong Python là một phương thức đặc biệt được gọi tự động khi một đối tượng mới của lớp được tạo ra. Nó thường được sử dụng để khởi tạo các thuộc tính của đối tượng.

#### Cấu trúc của Phương thức `__init__`

Phương thức `__init__` luôn có ít nhất một tham số là `self`. Tham số `self` đại diện cho đối tượng hiện tại và được sử dụng để truy cập các thuộc tính và phương thức của đối tượng.

##### Cú pháp cơ bản của `__init__`:

```python
class Car:
    # Hàm khởi tạo (constructor) để tạo ra các thuộc tính cho đối tượng
    def __init__(self, model, color):
        self.model = model  # Thuộc tính model
        self.color = color  # Thuộc tính color

    # Phương thức để mô phỏng hành vi lái xe
    def drive(self):
        print(f"{self.model} is driving")

    # Phương thức để mô phỏng hành vi dừng xe
    def stop(self):
        print(f"{self.model} has stopped")
```

Trong đó:

1. **Định nghĩa lớp `Car`**:
    - `__init__` là phương thức khởi tạo (constructor) đặc biệt trong Python. Nó được gọi khi một đối tượng mới của lớp được tạo ra. Phương thức này thường được sử dụng để khởi tạo các thuộc tính của đối tượng.
    - `self` là tham số đầu tiên trong tất cả các phương thức của lớp. Nó là tham chiếu đến đối tượng hiện tại của lớp và được sử dụng để truy cập các thuộc tính và phương thức của lớp.

2. **Tạo đối tượng `my_car`**:
    - `my_car = Car("Toyota", "Red")` tạo ra một đối tượng mới của lớp `Car` với các thuộc tính `model` là "Toyota" và `color` là "Red".

3. **Gọi các phương thức**:
    - `my_car.drive()` gọi phương thức `drive` của đối tượng `my_car`, in ra "Toyota is driving".
    - `my_car.stop()` gọi phương thức `stop` của đối tượng `my_car`, in ra "Toyota has stopped".


## Tính kế thừa

**Tính kế thừa** (inheritance) là một trong bốn tính chất cơ bản của lập trình hướng đối tượng (OOP), cùng với tính đóng gói (encapsulation), tính đa hình (polymorphism), và tính trừu tượng (abstraction). Tính kế thừa cho phép một lớp mới (lớp con hay subclass) thừa hưởng các thuộc tính và phương thức từ một lớp đã tồn tại (lớp cha hay superclass). Điều này giúp tái sử dụng mã, giảm bớt sự dư thừa, và tổ chức mã nguồn một cách logic hơn.

### Lợi ích của Tính Kế Thừa

1. **Tái sử dụng mã**: Các lớp con có thể sử dụng lại mã đã có trong lớp cha mà không cần phải viết lại.
2. **Dễ bảo trì**: Khi cần thay đổi hành vi chung, bạn chỉ cần thay đổi trong lớp cha, các lớp con sẽ tự động cập nhật theo.
3. **Mở rộng chức năng**: Các lớp con có thể thêm các thuộc tính và phương thức mới hoặc ghi đè (override) các phương thức của lớp cha.

### Cú pháp và Cách Sử Dụng

Trong Python, bạn có thể định nghĩa một lớp con bằng cách đặt tên lớp cha trong ngoặc đơn sau tên lớp con.

#### Ví dụ cơ bản về Tính Kế Thừa

```python
# Định nghĩa lớp cha
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Định nghĩa lớp con
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Tạo đối tượng từ lớp con
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Gọi phương thức của lớp con
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

### Giải thích chi tiết

1. **Định nghĩa lớp cha `Animal`**:
    - `__init__(self, name)` là phương thức khởi tạo nhận tham số `name`.
    - `speak(self)` là một phương thức trừu tượng (abstract method) được định nghĩa nhưng không có hành động cụ thể.

2. **Định nghĩa các lớp con `Dog` và `Cat`**:
    - `class Dog(Animal)` chỉ ra rằng `Dog` kế thừa từ `Animal`.
    - `speak(self)` trong lớp `Dog` và `Cat` ghi đè (override) phương thức `speak` của lớp cha `Animal`.

3. **Tạo đối tượng và sử dụng các lớp con**:
    - `dog = Dog("Buddy")` tạo một đối tượng `Dog` với tên "Buddy".
    - `cat = Cat("Whiskers")` tạo một đối tượng `Cat` với tên "Whiskers".
    - `dog.speak()` và `cat.speak()` gọi phương thức `speak` đã được ghi đè trong các lớp con.

### Tính Kế Thừa và Ghi Đè Phương Thức

Các lớp con có thể ghi đè các phương thức của lớp cha để cung cấp các hành vi cụ thể cho từng loại đối tượng.

#### Ví dụ về ghi đè phương thức:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Tạo đối tượng từ lớp Dog
dog = Dog("Buddy")

# Gọi phương thức speak
print(dog.speak())  # Output: Buddy says Woof!
```

#### Sử dụng `super()` để gọi phương thức của lớp cha

Khi ghi đè một phương thức, bạn có thể sử dụng `super()` để gọi phương thức của lớp cha. Điều này rất hữu ích khi bạn muốn mở rộng (mà không thay thế hoàn toàn) hành vi của phương thức lớp cha trong lớp con.

#### Ví dụ sử dụng `super()`:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Gọi phương thức __init__ của lớp cha
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"

# Tạo đối tượng từ lớp Dog
dog = Dog("Buddy", "Labrador")

# Gọi phương thức speak
print(dog.speak())  # Output: Buddy the Labrador says Woof!
```

#### Giải thích chi tiết về `super()`

1. **Khởi tạo lớp cha**:
    - `super().__init__(name)` gọi phương thức khởi tạo `__init__` của lớp cha `Animal` để khởi tạo thuộc tính `name`.

2. **Ghi đè và mở rộng phương thức**:
    - `speak(self)` trong lớp `Dog` ghi đè phương thức `speak` của lớp cha nhưng sử dụng thêm thuộc tính `breed` để cung cấp hành vi cụ thể hơn cho đối tượng `Dog`.

#### Một ví dụ phức tạp hơn về tính kế thừa

Giả sử chúng ta có một hệ thống quản lý nhân viên với các lớp `Employee`, `Manager`, và `Developer`.

#### Định nghĩa các lớp:

```python
class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id_number}"

class Manager(Employee):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, id_number, programming_language):
        super().__init__(name, id_number)
        self.programming_language = programming_language

    def get_details(self):
        return f"{super().get_details()}, Programming Language: {self.programming_language}"

# Tạo đối tượng từ các lớp con
manager = Manager("Alice", "M123", "HR")
developer = Developer("Bob", "D456", "Python")

# Gọi phương thức get_details
print(manager.get_details())  # Output: Name: Alice, ID: M123, Department: HR
print(developer.get_details())  # Output: Name: Bob, ID: D456, Programming Language: Python
```

#### Giải thích chi tiết

1. **Định nghĩa lớp `Employee`**:
    - `__init__(self, name, id_number)` khởi tạo các thuộc tính `name` và `id_number`.
    - `get_details(self)` trả về chi tiết của nhân viên.

2. **Định nghĩa lớp `Manager` kế thừa từ `Employee`**:
    - `__init__(self, name, id_number, department)` khởi tạo thêm thuộc tính `department` và gọi `super().__init__(name, id_number)` để khởi tạo các thuộc tính từ lớp cha.
    - `get_details(self)` ghi đè phương thức của lớp cha và sử dụng `super().get_details()` để lấy chi tiết từ lớp cha, sau đó thêm thông tin `department`.

3. **Định nghĩa lớp `Developer` kế thừa từ `Employee`**:
    - `__init__(self, name, id_number, programming_language)` khởi tạo thêm thuộc tính `programming_language` và gọi `super().__init__(name, id_number)` để khởi tạo các thuộc tính từ lớp cha.
    - `get_details(self)` ghi đè phương thức của lớp cha và sử dụng `super().get_details()` để lấy chi tiết từ lớp cha, sau đó thêm thông tin `programming_language`.

