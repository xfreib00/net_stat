#!/usr/bin/env python3
import sys
import pyspeedtest

#class for measuring internet dowload,upload and ping
class SP_Test: 

    #initialization of list and speedtest class
    def __init__(self):
        self.test_list = []
        self.st = pyspeedtest.SpeedTest()

    #measuring internet speeds and appeding results to the list
    def get_stats(self):
        self.test_list.append(self.st.download())
        self.test_list.append(self.st.upload())
        self.test_list.append(self.st.ping())    
    
    #removing all items from list
    def clear_list(self):
        self.test_list.clear()

#class for making stats from multiple tests
class Count_test(SP_Test):


