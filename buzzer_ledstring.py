import time
import board
import digitalio
import pwmio

# === Buzzer GP22 ===
buzzer_volume = 0.5  # Âm lượng (0.0 đến 1.0)
buzzer = pwmio.PWMOut(board.GP22, frequency=3000, duty_cycle=0)

# === Nút nhấn ở GP21 (cho buzzer) ===
button = digitalio.DigitalInOut(board.GP21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Nút nối xuống GND

# === Nút nhấn ở GP20 (cho LED) ===
button_rgb = digitalio.DigitalInOut(board.GP20)
button_rgb.direction = digitalio.Direction.INPUT
button_rgb.pull = digitalio.Pull.UP  # Nút nối xuống GND

# === LED thường GP0 -> GP6 ===
led_pins = [board.GP0, board.GP1, board.GP2, board.GP3,
            board.GP4, board.GP5, board.GP6]
leds = []
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

# === Thời gian debounce cho nút RGB (milliseconds) ===
debounce_time = 0.2  # Thời gian chống nhiễu 200ms
last_rgb_time = time.monotonic()  # Lưu thời gian nhấn nút RGB

# === Vòng lặp chính ===
while True:
    now = time.monotonic()

    # ===== Xử lý buzzer tức thời =====
    if not button.value:  # Nút nhấn (LOW) ở GP21
        buzzer.duty_cycle = int(65535 * buzzer_volume)  # Kêu buzzer
    else:
        buzzer.duty_cycle = 0  # Tắt buzzer

    # ===== LED chạy dải từ GP0 -> GP6 khi nhấn nút GP20 =====
    if not button_rgb.value and now - last_rgb_time > debounce_time:
        # Nếu nhấn nút GP20 và đã đủ thời gian debounce
        # Chạy dải màu LED từ GP0 đến GP6
        # LED chạy xuôi (từ GP0 đến GP6)
        for i in range(len(leds)):
            leds[i].value = True
            time.sleep(0.1)
            leds[i].value = False
        # LED chạy ngược (từ GP6 đến GP0)
        for i in reversed(range(len(leds))):
            leds[i].value = True
            time.sleep(0.1)
            leds[i].value = False

        last_rgb_time = now  # Cập nhật thời gian nhấn nút gần nhất
