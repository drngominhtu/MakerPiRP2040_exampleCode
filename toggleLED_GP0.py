import board
import digitalio
import time

# Khai báo LED GP0
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

# Khai báo nút GP21
button = digitalio.DigitalInOut(board.GP21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Trạng thái LED
led_state = False

while True:
    if not button.value:  # Nút nhấn (LOW)
        led_state = not led_state
        led.value = led_state

        while not button.value:  # Chờ nhả nút
            time.sleep(0.01)
        time.sleep(0.2)
