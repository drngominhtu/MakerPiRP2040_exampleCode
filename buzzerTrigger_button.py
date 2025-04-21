import board
import digitalio
import pwmio
import time

# Nút nhấn GP21
button = digitalio.DigitalInOut(board.GP21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Còi trên GP22 (sử dụng PWM để tạo âm thanh)
buzzer = pwmio.PWMOut(board.GP22, duty_cycle=0, frequency=500)

while True:
    if not button.value:  # Nếu nút được nhấn
        buzzer.duty_cycle = 32768  # Bật còi (50% duty cycle)
    else:
        buzzer.duty_cycle = 0  # Tắt còi

    time.sleep(0.01)  # Nhỏ delay để giảm tải CPU
