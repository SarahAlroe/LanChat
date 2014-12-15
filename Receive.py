# -*- coding: Utf-8 -*-
import json
import random
import select
import threading
import time
import sys
import traceback
import sys
class Receive (threading.Thread):
    def __init__(self,sock,client):
        #Init threading:
        threading.Thread.__init__(self)
        
        #instance of client for callback
        self.client = client
        
        #Take sock in as a variable
        self.sock = sock
        self.ap = self.client
        #Define global variables
        global out
        global msglist
        global connected
        connected = False
        global targetwindow

    def run(self):
        print "Starting receiving thread"
        while True:
            try:
                #Get new message:
                rec = self.sock.recvfrom(1024)
                
                #Extract data from rec:
                jout = rec[0]          
                #print "Rec: "+jout
                
                #Extract sender address from rec:
                sender=rec[1]
                
                #Turn Json to Dict:
                out = json.loads(jout, "utf-8")
                print "New rec, type: "+out["type"]

                print "Finding action"
                #What does this message contain?
                    #If it's a confirmation that a message has been received
                if out["type"] == "msg":
                    print "Recieved new message from "+out["username"]+"!"
                    self.ap.sm.get_screen("chat").chatDisplay.text += "\n"+out["username"]+": "+out["msg"]
                
                #elif out["type"] == "msg":
                #    print "Recieved new message from "+out["username"]+": "
                #    print out["msg"]
                #    self.ap.sm.get_screen("chat").ids.chatBox.text += "\n"+out["username"]+": "+out["msg"]
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)