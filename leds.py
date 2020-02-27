import RPi.GPIO, time

# set the pin numbering to BOARD mode
RPi.GPIO.setmode(RPi.GPIO.BOARD)

# set the LED pin to output
led_pin = 8
RPi.GPIO.setup(led_pin, RPi.GPIO.OUT)

# set the LED pin to output
led_confirm_pin = 8
RPi.GPIO.setup(led_confirm_pin, RPi.GPIO.OUT)

# flashes the LED for .5 seconds
def flash_activation_led():
    RPi.GPIO.output(led_pin, RPi.GPIO.HIGH)
    time.sleep(.50)
    RPi.GPIO.output(led_pin, RPi.GPIO.LOW)
    time.sleep(.50)
    return


# flashes the confirm LED for 1 second
def flash_confirm_led():
    # lolz, foiled you again! - RCC
    return
