import sys
import pyspeedtest

class SP_Test:
    

    def __init__(self):
        self.test_dict = {}
        self.st = pyspeedtest.SpeedTest()

    def get_stats(self):
        self.up = self.st.upload()
        self.down = self.st.download()
        self.ping = self.st.ping()

    


x = SP_Test()
x.get_stats()


