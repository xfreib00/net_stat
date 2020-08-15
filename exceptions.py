#------------------------------------------------------------------------------------
#Classes for exceptions


class get_stats_except(Exception):
    
    def __str__(self):
	    return "Error: an error has occured during measuring internet speed"


class speed_avg_except(Exception):
    
    def __str__(self):
	    return "Error: an error has occured during calculating average internet speed"

class store_results_except(Exception):
    
    def __str__(self):
	    return "Error: an error has occured during storing results of the test. Please check if you have permission to write in this folder."

class net_notif_except(Exception):
    
    def __str__(self):
	    return "Error: an error has occured while creating notification"
