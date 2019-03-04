import RPi.GPIO as GPIO
import time
import socket
import fcntl
import struct
import sys
import Adafruit_DHT
from RPLCD import CharLCD
from RPLCD.gpio import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11],
numbering_mode = GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd.cursor_pos = (0, 1)
lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
lcd.cursor_pos = (1, 0)
lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y"))
time.sleep(7)
lcd.clear()

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
lcd.cursor_pos = (0, 3)
lcd.write_string("Temp: %d C" % temperature)
lcd.cursor_pos = (1, 1)
lcd.write_string("Humidity: %d %%" % humidity)
time.sleep(7)
lcd.clear()

lcd.cursor_pos = (0, 2)
lcd.write_string("IP Address:") 
lcd.cursor_pos = (1, 2)
lcd.write_string(get_ip_address('wlan0'))
time.sleep(4)
lcd.clear()
lcd.cursor_pos = (0, 2)
lcd.write_string(u"Hello world!\n\rHow's it going?")
time.sleep(4)
lcd.clear()
lcd.write_string(u"Just got Working\n\rThis rlly cool!")
time.sleep(4)
lcd.clear()
lcd.write_string(u"Gunna clear the\n\rscreen now, Bye!")
time.sleep(4)
lcd.clear()
