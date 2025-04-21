import board
import digitalio
import neopixel
import time

# Khởi tạo 2 nút
btn1 = digitalio.DigitalInOut(board.GP20)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP21)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

# Khởi tạo 2 LED RGB
pixels = neopixel.NeoPixel(board.GP18, 2)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Đỏ, Xanh lá, Xanh dương
index1 = 0
index2 = 0

while True:
    if not btn1.value:
        index1 = (index1 + 1) % len(colors)
        pixels[0] = colors[index1]
        while not btn1.value:
            time.sleep(0.01)

    if not btn2.value:
        index2 = (index2 + 1) % len(colors)
        pixels[1] = colors[index2]
        while not btn2.value:
            time.sleep(0.01)

    time.sleep(0.1)
