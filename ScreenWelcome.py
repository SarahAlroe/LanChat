from kivy.uix.screenmanager import Screen, SlideTransition
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from uix.button import Button
kivy.require('1.8.0') # replace with your current kivy version !
class ScreenWelcome(Screen):
    
    def on_enter(self):
        self.add_widget(Button(text='Hello world 1'))
    
    