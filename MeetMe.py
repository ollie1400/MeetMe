# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:08:12 2016

@author: otlg1
"""

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from vectoriseevents import VectoriseEvents

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def SetupConnection():

    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    
    # "credentials" now contains the credentials
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    print('Service connected')
    return service;



def main():
    service = SetupConnection()
    
    print('Downloading free/busy information')
    
    
    
#    print('Downloading free/busy information')
#
#    calid = input("Enter your calendar id (probably your e-mail address): ");
#    fbquery = {
#        "timeMin" : "2016-05-21T12:15:21.848000Z",
#        "timeMax" : "2016-05-29T12:14:21.848000Z",
#        "items" : [
#            {
#                "id" : calid
#            }
#        ]
#    }
#    
#    fbdata = service.freebusy().query(body=fbquery).execute()
#    print(fbdata)

    print('Downloading event information')


    tmin = "2016-05-21T12:15:21.848000Z";
    tmax = "2016-05-29T12:15:21.848000Z";
    
    tmin = datetime.datetime.utcnow();
    tmax = t1 + datetime.timedelta(days=7)
    
    tminstr = tmin.isoformat() + 'Z'
    tmaxstr = tmax.isoformat() + 'Z'
    
    edata = service.events().list(calendarId="primary",timeMin=tminstr,timeMax=tmaxstr).execute()
    print(edata)
    
    # vectorise the events
    VectoriseEvents(edata,1,tmin,tmax)
    
if __name__ == '__main__':
    main()