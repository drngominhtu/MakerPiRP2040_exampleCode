import board
import digitalio
import time

# Tạo danh sách các chân LED
led_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7]
leds = []

# Khởi tạo LED
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

# Vòng lặp Knight Rider
while True:
    # Sang trái
    for i in range(len(leds)):
        leds[i].value = True
        time.sleep(0.05)
        leds[i].value = False

    # Sang phải
    for i in reversed(range(len(leds))):
        leds[i].value = True
        time.sleep(0.05)
        leds[i].value = False
