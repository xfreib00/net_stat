#!/usr/bin/env python3
import sys
import pyspeedtest
import json
import notify2
from datetime import datetime
from statistics import mean

#------------------------------------------------------------------------------------
#Classes for exceptions

class get_stats_except(Exception):
    pass

class speed_avg_except(Exception):
    pass

class store_results_except(Exception):
    pass

class net_notif_except(Exception):
    pass

#-------------------------------------------------------------------------------------
#class for measuring internet dowload,upload and ping
class SP_Test: 
    
    #initialization of list and speedtest class
    def __init__(self):
        self.test_list = []
        self.st = pyspeedtest.SpeedTest()

    #measuring internet speeds and appeding results to the list
    def get_stats(self):
        try:
            self.test_list.append(self.st.download())
            self.test_list.append(self.st.upload())
            self.test_list.append(self.st.ping())    
        except:
            raise get_stats_except()

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
        except:
            raise speed_avg_except()


    #printing result of average speeds
    #strictly debugging function
    def print_results(self):
        print(*self.result_list)

    def store_results(self):
        try:
            self.net_notif("Started")
            self.speed_avg()
            f = open('stats.json','a+')
            time_now = (str(datetime.now())).split(' ')[0]
            json.dump({'date':time_now,'download':self.result_list[0],'upload':self.result_list[1],'ping':self.result_list[2]},f)
            f.close()
            self.net_notif("Finished")
        except:
            raise store_results_except()

    def net_notif(self,message):
        try:
            notify2.init("Net Stats")
            n = notify2.Notification("Net Stats","%s test"%(message))
            n.show()
        except:
            raise net_notif_except()
            
#---------------------------------------------------------------------------------------

#TODO create class for reading file filled with json

class Read_stats:
    def __init__():
        with open('stats.json','r') as js_file:
            self.data = js_file.read()

    def read_file():
        self.js_obj = json.loads(self.data)
        


#TODO create class for making statistics

#creating object of Count_test class and running speed tests
try:
    X = Count_test()
    X.store_results()

#in case of Keyboard interrupt exit program immediately
except KeyboardInterrupt:
    exit(0)
except net_notif_except:
    exit(10)
except store_results_except:
    exit(11)
except speed_avg_except:
    exit(12)
except get_stats_except:
    exit(13)
except SystemExit as ex:
    exit(ex.code)




