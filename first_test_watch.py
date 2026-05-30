from machine import Pin, I2C
import ssd1306
import network
import ntptime
import time

# OLED
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# WiFi
ssid = ""
password = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

oled.fill(0)
oled.text("Forbinder WiFi...", 0, 0)
oled.show()

while not wifi.isconnected():
    time.sleep(1)

oled.fill(0)
oled.text("WiFi OK", 0, 0)
oled.show()
time.sleep(1)

# Hent tid fra NTP
ntptime.settime()

while True:
    # dansk sommertid
    t = time.localtime(time.time() + 7200)

    hour = t[3]
    minute = t[4]
    second = t[5]
    day = t[2]
    month = t[1]
    year = t[0]

    klokke = "{:02}:{:02}:{:02}".format(hour, minute, second)
    dato = "{:02}-{:02}-{}".format(day, month, year)

    oled.fill(0)
    oled.text("Current Time", 0, 0)
    oled.text(klokke, 0, 20)
    oled.text(dato, 0, 40)
    oled.show()

    time.sleep(1)
