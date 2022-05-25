# MultiThreading

from concurrent.futures import thread
from ntpath import join
import threading
from threading import *
from time import sleep


class white (Thread) :   # Passing Thread as argument
    def run (self) :
        for i in range(5) :
            print("white")
            sleep(1)     # sleep for 1 second 
        

class black (Thread) :   # Passing Thread as argument
    def run (self) :
        for i in range(5) :
            print("black")  
            sleep(1)     # sleep for 1 second 


wht = white()
blk = black()

wht.start()       # instead of wht.run
sleep(0.2)
blk.start()       # instead of blk.run

wht.join()        # main thread will wait for wht.start() to complete
blk.join()        # main thread will wait for blk.start() to complete

print("Ending")   # main thread will print "Ending" once wht.start() and blk.start() is complete