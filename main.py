from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from sitish import *

class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.anchor_layout = AnchorLayout()
        self.button = Button(text="Menu sitishs", size_hint=(None, None), size=(200, 50))
        self.button.bind(on_press=self.new_label)
        self.anchor_layout.add_widget(self.button)
        self.add_widget(self.anchor_layout)

    def new_label(self, button):
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

    def reset_screen(self, button):
        self.anchor_layout.clear_widgets()
        self.anchor_layout.add_widget(self.button)

class Services(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    Services().run()

