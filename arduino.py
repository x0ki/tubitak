import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    board.digital[2].write(1)
    time.sleep(1)
    board.digital[2].write(0)
    time.sleep(1)