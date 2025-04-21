import board
import digitalio
import time

# LED trên GP0–GP7
led_pins = [board.GP0, board.GP1, board.GP2, board.GP3,
            board.GP4, board.GP5, board.GP6, board.GP7]
leds = [digitalio.DigitalInOut(pin) for pin in led_pins]
for led in leds:
    led.direction = digitalio.Direction.OUTPUT

# Nút tăng (dùng GP20)
button = digitalio.DigitalInOut(board.GP20)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

counter = 0

while True:
    if not button.value:
        counter = (counter + 1) % 256  # 8-bit
        # Hiển thị ra LED
        for i in range(8):
            leds[i].value = (counter >> i) & 1

        while not button.value:
            time.sleep(0.01)
        time.sleep(0.1)
