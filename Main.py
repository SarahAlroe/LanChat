from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.image import Image
import kivy
from ScreenWelcome import ScreenWelcome
from ScreenChat import ScreenChat
import json
from Receive import Receive
import socket
import sys

kivy.require('1.8.0') # replace with your current kivy version !

# Create the screen manager


class SoundMemoryGameApp(App):
    def build(self):
        Config.set('graphics', 'fullscreen', "0")
        Config.write()
        self.title = 'LanChat'
        self.sm = ScreenManager()
        self.sm.add_widget(ScreenWelcome(name='welcome'))
        self.sm.add_widget(ScreenChat(name='chat'))
        
        return self.sm

    def initializeConnection(self):
        # set sock
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", self.port))
        self.sock.setblocking(0)
        self.sock.settimeout(20)

    #Called automatically when app is started
    def on_start(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        #show the first screen:
        App.get_running_app().sm.current = "welcome"
        with open("contacts.txt") as f:
            self.contacts = f.readlines()
        cleancontacts=[]
        for ipadr in self.contacts:
            cleancontacts.append(ipadr.replace("\n",""))
        self.contacts=cleancontacts
        print self.contacts
        self.port=5008
        self.initializeConnection()
        self.receiver = Receive(self.sock,self)
        self.receiver.start()


    def sendMsg(self, message):
        data = {'type':"msg", 'username':self.username, 'msg':message}
        jdata = json.dumps(data, ensure_ascii=False)
        print"Sending message!"
        for ip in self.contacts:
            self.send(jdata, ip)

    def send(self, data, reciever):
        self.sock.sendto(data,(reciever,self.port))

    ''' 
    Navigate the user back to the welcome screen
    '''       
    def on_back(self):
        App.get_running_app().sm.current = "welcome"

if __name__ == '__main__':
    SoundMemoryGameApp().run()