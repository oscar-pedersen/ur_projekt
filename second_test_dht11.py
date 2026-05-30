#andet test program til DHT11 sensor ur upgradering
from machine import Pin, I2C
import ssd1306
import dht
import time

# OLED
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# DHT11
sensor = dht.DHT11(Pin(12))   # D6

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()

    oled.fill(0)
    oled.text("Room Climate", 0, 0)
    oled.text("Temp: {} C".format(temp), 0, 20)
    oled.text("Hum : {} %".format(hum), 0, 35)
    oled.show()

    time.sleep(2)
