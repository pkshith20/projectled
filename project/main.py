import machine
import time

def create_led(pin_list, delay_list):
    led_list = []
    for pin, delay in zip(pin_list, delay_list):
        led = machine.Pin(pin, machine.Pin.OUT)
        led_list.append((led, delay))
    return led_list

# example usage
led_pin_list = [1, 5 ]
led_delay_list = [1, 2]
led_list = create_led(led_pin_list, led_delay_list)

while True:
    for led, delay in led_list:
        led.toggle()
        time.sleep(delay)
        led.off()