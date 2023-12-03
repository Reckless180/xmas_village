from machine import Pin, UART, I2C
from time import sleep, sleep_ms, sleep_us

# Check RTC and set pico  clock
rtcAddr = 104
rtc = I2C(0, sda=Pin(16), scl=Pin(17), freq=50_000)


# 1Hz Square wave
rtc.writeto(104, b'\x07\x10')
# Start clock
rtc.writeto(104, b'\x00\x00')

