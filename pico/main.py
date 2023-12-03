from machine import Pin, UART, I2C
import binascii
from time import sleep, sleep_ms, sleep_us

# Check RTC and set pico  clock
rtcAddr = 104
rtc = I2C(0, sda=Pin(16), scl=Pin(17), freq=50_000)

def init():
    # Check the status of the Hardware RTC, set time if needed
    try:
        rtc.writeto(rtcAddr, b'\x00')
        rtcStatus = rtc.readfrom(rtcAddr, 1)
        clk_en = ord(rtcStatus) >> 7
        if clk_en == 0:
            print("Running")
        else:
            # 1Hz Square wave
            rtc.writeto(104, b'\x07\x10')
            print("RTC not set\n\n")
            print("Enter seconds: ")
            seconds = input()
            print(seconds)
            # Start clock
            rtc.writeto(104, b'\x00' + ord(seconds))
    except:
        return False
    return rtcStatus
         

def updateCountdown():
    # Count number of days until christmas and update the LED display driver
    pass

init()
while True:
    rtc.writeto(104,b'\x00')
    test = rtc.readfrom(104,1)
    print(binascii.hexlify(test.decode()))
    sleep_ms(500)
