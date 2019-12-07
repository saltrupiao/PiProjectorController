#!/usr/bin/env python
#turn Picture on
import sys
import serial


port = serial.Serial('/dev/ttyAMA0', baudrate=115200, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=5)

port.open

#this is the code sent to the projector.  Replace it for your model
#port.write("\x06\x14\x00\x04\x00\x34\x12\x09\x01\x67")

port.write("BLK0")
received = port.read(8)
print(received) # newline is printed

port.close
