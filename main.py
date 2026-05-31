from machine import Pin, I2C
import ssd1306
import dht
import network
import ntptime
import time

#knap
button = Pin(14,Pin.IN) #D5 på esp8266

# OLED
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


# DHT11
sensor = dht.DHT11(Pin(12))

# WiFi
ssid = "YOUR SSID"
password = "YOUR PASSWORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

oled.fill(0)
oled.text("Tjekker WIFI...", 0, 0)
oled.show()

while not wifi.isconnected():
    time.sleep(1)

ntptime.settime()

while True:
    #tjek om knappen er trykket
    if button.value() == 1:
        #klokken interface
        for _ in range(5):
            t = time.localtime(time.time() + 7200)  # dansk sommertid
            klokke = "{:02}:{:02}:{:02}".format(t[3], t[4], t[5])
            dato = "{:02}-{:02}-{}".format(t[2], t[1], t[0])
            oled.fill(0)
            oled.text("CURRENT TIME", 0, 0)
            oled.text(klokke, 18, 20)
            oled.text(dato, 12, 40)
            oled.show()
            time.sleep(0.5)
    else:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        oled.fill(0)
        oled.text("Room Climate", 0, 0)
        oled.text("Temp: {} C".format(temp), 0, 20)
        oled.text("Hum : {} %".format(hum), 0, 35)
        oled.show()

        time.sleep(0.5)
        
        
