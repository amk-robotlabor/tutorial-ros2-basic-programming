import random
import time

import serial
import asyncio


async def main():
    port = 'COM4'
    loop = asyncio.get_event_loop()
    servo0 = random.randint(0, 180)
    servo1 = random.randint(0, 180)
    cmd = f"{servo0};{servo1}\r\n"




    async def read_serial():
        txt = ""
        msg = ser.read().decode()
        while msg != '\n':
            txt += msg
            msg += ser.read().decode()




    with serial.Serial(port, 9600, timeout=1) as ser:

        print(cmd.encode())

        ser.write(cmd.encode())
        try:
            await read_serial()
        except KeyboardInterrupt:
            pass
        finally:
            loop.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
