#!/usr/bin/env python3
import sys
import pyspeedtest
import json
import notify2
from datetime import datetime
from statistics import mean

#-------------------------------------------------------------------------------------
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
    
#--------------------------------------------------------------------------------------
#class for making stats from multiple tests
class Count_test(SP_Test):

    #creating 3 objects of SP_Test class and list for results
    def __init__(self):
        self.t1 = SP_Test()
        self.t2 = SP_Test()
        self.t3 = SP_Test()
        self.result_list = []

    #counting the average down,up and ping from 3 tests
    def speed_avg(self):
        try:
            self.t1.get_stats()
            self.t2.get_stats()
            self.t3.get_stats()
            self.result_list = [mean(k) for k in zip(self.t1.test_list,self.t2.test_list,self.t3.test_list)]
        #TODO make exception handler
        except:
            exit(1)


    #printing result of average speeds
    #strictly debugging function
    def print_results(self):
        print(*self.result_list)

    def store_results(self):
        try:
            self.net_notif("Started")
            self.speed_avg()
            f = open('stats','a+')
            time_now = (str(datetime.now())).split(' ')[0]
            json.dump({'date':time_now,'download':self.result_list[0],'upload':self.result_list[1],'ping':self.result_list[2]},f)
            f.close()
            self.net_notif("Finished")
        except OSError:
            exit(1)

    def net_notif(self,message):
        notify2.init("Net Stats")
        n = notify2.Notification("Net Stats","%s test"%(message))
        n.show()

#---------------------------------------------------------------------------------------
#creating object of Count_test class and running speed tests
try:
    X = Count_test()
    X.store_results()

#in case of Keyboard interrupt exit program immediately
except KeyboardInterrupt:
    exit(0)






