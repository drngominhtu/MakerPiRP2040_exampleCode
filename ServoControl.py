import board
import digitalio
import pwmio
import time
from adafruit_motor import servo

# Nút nhấn GP20 (xoay tới) và GP21 (xoay lui)
button_forward = digitalio.DigitalInOut(board.GP20)
button_forward.direction = digitalio.Direction.INPUT
button_forward.pull = digitalio.Pull.UP

button_backward = digitalio.DigitalInOut(board.GP21)
button_backward.direction = digitalio.Direction.INPUT
button_backward.pull = digitalio.Pull.UP

# Servo gắn GP1
pwm_servo = pwmio.PWMOut(board.GP12, frequency=50)  # 50Hz
my_servo = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

# Góc hiện tại của servo
servo_angle = 0
my_servo.angle = servo_angle

while True:
    if not button_forward.value:  # Nút GP20 nhấn
        servo_angle = 100
        my_servo.angle = servo_angle
        while not button_forward.value:
            time.sleep(0.01)

    if not button_backward.value:  # Nút GP21 nhấn
        servo_angle = 0
        my_servo.angle = servo_angle
        while not button_backward.value:
            time.sleep(0.01)

    time.sleep(0.01)
