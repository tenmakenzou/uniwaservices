#gui related
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

import webbrowser

#python script related
from sitish import *
from library import *

class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        self.buttons_layout = BoxLayout(orientation='vertical', size_hint=(None, None), spacing=10)
        self.buttons_layout.size = (200, 180)  # Adjust size to fit buttons and spacing

        self.button = Button(text="Restauraunt Menu\nΠρογραμμα Σίτισης", size_hint=(None, None), size=(200, 50))
        self.button2 = Button(text="Library / Restauraunt opening\nΒιβλιοθήκη / Λέσχη ωράριο", size_hint=(None, None), size=(200, 50))
        self.button3 = Button(text="Services", size_hint=(None, None), size=(200, 50))

        self.button.bind(on_press=self.sitish)
        self.button2.bind(on_press=self.schedule)
        self.button3.bind(on_press=self.services)

        self.buttons_layout.add_widget(self.button)
        self.buttons_layout.add_widget(self.button2)
        self.buttons_layout.add_widget(self.button3)

        self.anchor_layout.add_widget(self.buttons_layout)
        self.add_widget(self.anchor_layout)

    def sitish(self, button):
        self.anchor_layout.clear_widgets()
        self.grid_layout = GridLayout(cols=1, spacing=0, size_hint=(1, 1))
        self.label = Label(text=run(), text_size=(None, None), halign='center', valign='middle', size_hint=(1, 0.9))
        self.label.bind(size=self.label.setter('text_size'))
        self.back_button = Button(text="Back", size_hint=(None, None), size=(200, 50))
        self.back_button.bind(on_press=self.reset_screen)

        back_button_anchor = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(1, 0.1))
        back_button_anchor.add_widget(self.back_button)

        self.grid_layout.add_widget(self.label)
        self.grid_layout.add_widget(back_button_anchor)
        self.anchor_layout.add_widget(self.grid_layout)

    def schedule(self, button):
        self.anchor_layout.clear_widgets()
        self.grid_layout = GridLayout(cols=1, spacing=0, size_hint=(1, 1))

        self.label = Label(text=get_library(), text_size=(None, None), halign='center', valign='middle', size_hint=(1, 0.5))
        self.label.bind(size=self.label.setter('text_size'))
        self.label2 = Label(text=get_restauraunt(), text_size=(None, None), halign='center', valign='middle', size_hint=(1, 0.5))
        self.label2.bind(size=self.label.setter('text_size'))

        self.back_button = Button(text="Back", size_hint=(None, None), size=(200, 50))
        self.back_button.bind(on_press=self.reset_screen)

        back_button_anchor = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(1, 0.1))
        back_button_anchor.add_widget(self.back_button)

        self.grid_layout.add_widget(self.label)
        self.grid_layout.add_widget(self.label2)
        self.grid_layout.add_widget(back_button_anchor)
        self.anchor_layout.add_widget(self.grid_layout)

    def services(self, button):
        self.anchor_layout.clear_widgets()
        self.grid_layout = GridLayout(cols=1, spacing=10, size_hint=(None, None), size=(200, 180))

        eclass_button = Button(text="Eclass", size_hint=(None, None), size=(200, 50))
        eclass_button.bind(on_press=lambda x: webbrowser.open("https://eclass.uniwa.gr/"))

        services_button = Button(text="Services", size_hint=(None, None), size=(200, 50))
        services_button.bind(on_press=lambda x: webbrowser.open("https://sso.uniwa.gr/login?service=https%3A%2F%2Fservices.uniwa.gr%2Flogin%2Fcas"))

        self.back_button = Button(text="Back", size_hint=(None, None), size=(200, 50))
        self.back_button.bind(on_press=self.reset_screen)

        buttons_anchor = AnchorLayout(anchor_x='center', anchor_y='center')
        buttons_anchor.add_widget(self.grid_layout)

        self.grid_layout.add_widget(eclass_button)
        self.grid_layout.add_widget(services_button)
        self.grid_layout.add_widget(self.back_button)

        self.anchor_layout.add_widget(buttons_anchor)

    def reset_screen(self, button):
        self.anchor_layout.clear_widgets()
        self.buttons_layout.clear_widgets()
        self.buttons_layout.add_widget(self.button)
        self.buttons_layout.add_widget(self.button2)
        self.buttons_layout.add_widget(self.button3)
        self.anchor_layout.add_widget(self.buttons_layout)

class Services(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    Services().run()
