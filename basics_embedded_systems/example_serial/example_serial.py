import random
import time

import serial


def main():
    port = 'COM4'

    with serial.Serial(port, 9600, timeout=1) as ser:

        if ser.is_open:
            print("Port is open")
            servo0 = random.randint(0, 180)
            servo1 = random.randint(0, 180)
            cmd = f"{servo0};{servo1}\r\n"
            ser.write(cmd.encode())
            print(cmd.encode())
            line = ser.read(10)
            time.sleep(1)
            print(line)


        else:
            print("Port is closed")



if __name__ == "__main__":
    main()
