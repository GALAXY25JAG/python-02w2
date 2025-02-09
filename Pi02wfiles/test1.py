from smbus import SMBus
import time 

I2C_ADDR = 0x27 # bus address
I2C_BUS = 1

bus = SMBus(I2C_BUS)

def lcd_write(text):
    for char in text:
        bus.write_byte(I2C_ADDR, ord(char))
        time.sleep(0.01)

def main():
    lcd_write("\x0C")
    time.sleep(0.5)

    message = "Hello World"
    lcd_write(message)

if __name__=="__main__":
    main()