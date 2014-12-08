from kivy.uix.screenmanager import Screen, SlideTransition
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

kivy.require('1.8.0') # replace with your current kivy version !

class ScreenChat(Screen):
    
    def on_enter(self):
        self.verticalLayout=BoxLayout(orientation="vertical",padding=[25,25,25,25], spacing=[100,100])
        self.horizontalLayout=BoxLayout(orientation="horizontal", size_hint_y=0.25,padding=[0,25,0,0], spacing=[25,25])
        self.chatDisplay=TextInput(font_name="VT323.ttf",multiline=True, readonly=True, foreground_color=[0,1,0,1], background_normal="Green border.png", background_active="Green border.png", border=(6,6,6,6))
        self.messageInput=TextInput(font_name="VT323.ttf",multiline=False, foreground_color=[0,1,0,1], background_normal="Green border.png", background_active="Green border.png", border=(6,6,6,6))
        self.sendButton=Button(text="Send!",font_name="VT323.ttf",background_normal="Green border.png", background_down="Green border.png", border=[6,6,6,6],size_hint_x=0.25, halign="center", color=[0,1,0,1])
        self.verticalLayout.add_widget(self.chatDisplay)
        self.horizontalLayout.add_widget(self.messageInput)
        self.horizontalLayout.add_widget(self.sendButton)
        self.verticalLayout.add_widget(self.horizontalLayout)
        self.add_widget(self.verticalLayout)
        self.sendButton.bind(on_press=self.sendMsg)
        self.messageInput.bind(on_text_validate=self.sendMsg)
        self.refocusMessageInput()
    
    def sendMsg(self,mess):
        if self.messageInput.text !="":
            print"Sending message: "+self.messageInput.text
            App.get_running_app().sendMsg(self.messageInput.text)
        self.messageInput.text=""
        Clock.schedule_once(self.refocusMessageInput)

    def refocusMessageInput(self,*args):
        self.messageInput.focus = True