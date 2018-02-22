#!/usr/bin/env python

from pymultiwii import MultiWii
import time
n=0

if __name__ == "__main__":

    #board = MultiWii("/dev/tty.usbserial-AM016WP4")
    board = MultiWii("/dev/rfcomm0")
    try:
        board.arm()
        print "Board is armed now!"
        while n<10 :
	        data = [1500,1500,1500,2000,1500,1500,1500,1500]
	        board.sendCMD(16,MultiWii.SET_RAW_RC,data)
	        time.sleep(1)
	        print "go"
	        n+=1
        print "Board is disarmed now!"
        board.disarm()

    except Exception,error:
        print "Error on Main: "+str(error)
