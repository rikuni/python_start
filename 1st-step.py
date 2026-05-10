import time
import random

# pythonには変数の型宣言不要
x = 10
y = 3.14
name = "sensor"

# pythonの条件分岐 {}不要、インデントでifブロックを示す、elifはelse ifの略
value = 80
if value > 100:
    print("ERROR")
elif value > 70:
    print("WARNING")
else:
    print("OK")

for i in range(5):
    print(i)

i = 0

while i < 5:
    print(i)
    i += 1

data = [10, 20, 30]

data.append(40)
print(data)

data = [1, 2, 3, 4, 5]

print(len(data))   # 長さ
print(data[0])     # 先頭
print(data[-1])    # 末尾


data = [0, 1, 2, 3, 4, 5]

print(data[1:4])   # [1,2,3]
print(data[:3])    # [0,1,2]
print(data[::2])   # 1つ飛ばし

def add(a, b):
    return a + b

result = add(3, 5)
print(result)


def set_speed(speed=50):
    print(speed)

set_speed()
set_speed(80)


class Motor:
    def __init__(self):
        self.speed = 0

    def set_speed(self, value):
        self.speed = value
        print("speed:", self.speed)

m = Motor()
m.set_speed(30)      


sensor = 85

if sensor > 100:
    print("FAULT")
elif sensor > 70:
    print("WARN")
else:
    print("NORMAL")

data = [10, 20, 30, 40, 50]

high = [x for x in data if x > 25]
print(high)    

print("Hello World")