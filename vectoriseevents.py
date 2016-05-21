# -*- coding: utf-8 -*-
"""
Take the event structure from Gogle and make it into a "busy" vector


@author: otlg1
"""

from scipy.sparse import csr_matrix
import datetime;
from numpy import floor

"""
Take the events structure and make it into a "busy" vector.
@dt is the discretisation time in hours (e.g. 0.5 = 30mins)
"""
def VectoriseEvents(events,dt,timeMin,timeMax):
    
    # round the min/max time to the lowest hour
    timeMinRounded = RoundDateTime(timeMin,0)
    timeMaxRounded = RoundDateTime(timeMax,0)
    
    
    # intervals between 
    nIntervals = floor(IntervalsBetweenDateTimes(timeMin, timeMax, 1))
    
    # vectorised times
    busy = csr_matrix((1,nIntervals));
    
    # how many entries?
    nentries = len(events['items'])
    for i in range(0,nentries):
        
        pass
        
    
    return 0;
    

"""
We take a datetime timestamp, round it down to the nearest "minsToRoundTo" centered on the hour.
For now just round to the lowest hour, so just discard the minutes etc.
"""
def RoundDateTime(tm, minsToRoundTo):
    discard = datetime.timedelta(minutes=tm.minute,# % minsToRoundTo,
                             seconds=tm.second,
                             microseconds=tm.microsecond)
    tm -= discard
    #if discard >= datetime.timedelta(minutes=5):
    #    tm += datetime.timedelta(minutes=10)
        
    return tm
    
"""
How many time intervals of dt between two datetimes?
@dt is time interval in seconds
"""
def IntervalsBetweenDateTimes(t1, t2, dt):
    numIntervals = (t2 - t1).total_seconds() / (3600  * dt)
    return numIntervals
    
    
    
def main():
        
    t1 = datetime.datetime.now();
    t2 = t1 + datetime.timedelta(days=1)
    
    VectoriseEvents(0, 1, t1, t2)
if __name__ == '__main__':
    main()