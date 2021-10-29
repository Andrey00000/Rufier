from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Sc1(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
       
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(Label(text = '''Данное приложение позволит вам с помощью теста Руфье
        
        '''))
        b = Button(text= "Вперёд!", size_hint = (.5, None), height='60sp', pos_hint ={'left': 1} )
        b.on_press = self.next
        
        self.add_widget(box)
        ti = TextInput(text= 'Введите имя', size_hint = (1, None), height='30sp',halign='left', focus=True, multiline=False)
        box.add_widget(ti)
        box.add_widget(b)
    def next(self, *args, **kwargs):
        self.manager.current = 'Sc2'
       

class Sc2(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(Label(text = 'Второй экран'))
        b = Button(text= "Вперёд!", size_hint = (1, None), height='60sp')
        b.on_press =self.next
        box.add_widget(b)
        self.add_widget(box)
    def next(self, *args, **kwargs):
        self.manager.current = 'Sc3'

class Sc3(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(Label(text = 'Третий экран'))
        b = Button(text= "Вперёд!", size_hint = (1, None), height='60sp' )
        b.on_press =self.next
        box.add_widget(b)
        self.add_widget(box)
    def next(self, *args, **kwargs):
        self.manager.current = 'Sc4'
class Sc4(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(Label(text = 'Четвёртый экран'))
        b = Button(text= "Вперёд!", size_hint = (1, None), height='60sp' )
        b.on_press =self.next
        box.add_widget(b)
        self.add_widget(box)
    def next(self, *args, **kwargs):
        self.manager.current = 'Sc5'
class Sc5(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        b = Button(text="dhbhfb")
        b.on_press =self.next
        self.add_widget(b)
    def next(self, *args, **kwargs):
        self.manager.current = 'Sc6'

class MyApp(App):
    def build(self):
        self.manager = ScreenManager()
        self.manager.add_widget(Sc1(name = 'Sc1'))
        self.manager.add_widget(Sc2(name = 'Sc2'))
        self.manager.add_widget(Sc3(name = 'Sc3'))
        self.manager.add_widget(Sc4(name = 'Sc4'))
        self.manager.add_widget(Sc5(name = 'Sc5'))

        return self.manager
app = MyApp()
app.run()
        
