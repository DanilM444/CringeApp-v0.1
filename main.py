from kivy.app import App 
from kivy.uix.button import Button  
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.floatlayout import FloatLayout


class Container(FloatLayout):
    pass


class CringeApp(App):  
    def build(self):  
        return Container()
    

if __name__ == '__main__': 
    CringeApp().run()
