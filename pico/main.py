from machine import Pin, UART, I2C
from time import sleep, sleep_ms, sleep_us
import network
import rp2
import urequests

# Check RTC and set pico  clock
rtcAddr = 104
rtc = I2C(0, sda=Pin(16), scl=Pin(17), freq=50_000)

# Networking information
rp2.country('CA')
ssid = "labswitch"
password = "3588ve3cuf"
apiServer = "http://192.168.0.16:3000/api/sync"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect of fail
max_wait = 10
while max_wait > 0:
    if wlan.status() <0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
    sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0] )

def updateCountdown():
    # Count number of days until christmas and update the LED display driver
    try:
        req = urequests.get(apiServer)
        data = req.json()
        month = data["date"][5:7]
        if month == "12":
            day = data["date"][8:10]
            count = 25 - int(day)
        else:
            print("Too early brah!")
            count = False
        return count
    except:
        return False

while True:
    countdown = updateCountdown()
    if (countdown):
        print("Ahhh ya only " + str(countdown) + " Days left!")
    else:
        print("Failed to connect.. retrying")
    sleep(15)

