from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.image import Image
import kivy
from ScreenWelcome import ScreenWelcome
from ScreenChat import ScreenChat


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
    
    #Called automatically when app is started
    def on_start(self):
        #show the first screen:
        App.get_running_app().sm.current = "welcome"  
        pass
    ''' 
    Navigate the user back to the welcome screen
    '''       
    def on_back(self):
        App.get_running_app().sm.current = "welcome"

if __name__ == '__main__':
    SoundMemoryGameApp().run()