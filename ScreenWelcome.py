from kivy.uix.screenmanager import Screen, SlideTransition
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from uix.button import Button
from uix.label import Label
from uix.anchorlayout import AnchorLayout
from uix.gridlayout import GridLayout
from uix.textinput import TextInput
kivy.require('1.8.0') # replace with your current kivy version !
class ScreenWelcome(Screen):
    
    def on_enter(self):
        self.anchorLayout = AnchorLayout(anchor_x="center", anchor_y="center")
        self.gridLayout = GridLayout(cols=1, padding=[100,100,100,100], spacing=[10,20])
        self.label = Label(text='LanChat', font_name="VT323.ttf", color=[0,1,0,1], font_size="150sp", size_hint_y=0.5, halign="center", pos_hint={'top':1})
        self.userNameInput = TextInput(hint_text='User Name', font_name="VT323.ttf", multiline=False,foreground_color=[0,1,0,1], hint_text_color=[0,1,0,0.5], cursor_color=[0,1,0,0.75], background_normal="Green border.png", background_active="Green border.png", border=(6,6,6,6), size_hint_x=0.5, size_hint_y=0.1,halign="center")
        self.chatButton = Button(text='Chat',font_name="VT323.ttf", size_hint_x=0.5, size_hint_y=0.1,background_normal="Green border.png", background_down="Green border.png", border=[6,6,6,6],color=[0,1,0,1])
        self.add_widget(self.gridLayout)
        self.gridLayout.add_widget(self.label)
        self.gridLayout.add_widget(self.userNameInput)
        self.gridLayout.add_widget(self.chatButton)
        self.chatButton.bind(on_press=self.chatButtonPressed)
    
    def chatButtonPressed(self,button):
        userName=self.getUserName()
        App.get_running_app().sm.current = "chat"
        
    def getUserName(self):
        if self.userNameInput.text!=None:
            userName=self.userNameInput.text
        else:
            userName = "Unnamed"
        return userName