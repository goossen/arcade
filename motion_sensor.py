import RPi.GPIO as GPIO
import time

#assign GPIO pins
pir_sensor = 12
led = 5

#on/off interval
minutes = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pir_sensor, GPIO.IN)

#initialize states
current_state = 0
GPIO.output(led, True)  #turn off

def checkMotionDuringTime() :
    print("checking for 10 minutes")
    count = 0;
    total = minutes * 60 * 10 # minutes * 60 seconds per minute * intervals per second
    while count < total:
        time.sleep(0.1)
        count+=1
        #check the PIR, returns 1 when motion detected
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            GPIO.output(led, False) #turn on
            count = 0;


print("waiting for PIR")

try:
    while True:
        time.sleep(0.1)
        checkMotionDuringTime()
        GPIO.output(led, True) #turn off

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
