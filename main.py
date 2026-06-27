from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(App):

    def button_click(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""

        elif text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"

        else:
            self.display.text += text

    def build(self):
        root = BoxLayout(orientation="vertical")

        self.display = TextInput(
            text="",
            readonly=True,
            font_size=40,
            halign="right",
            size_hint=(1, 0.2)
        )

        root.add_widget(self.display)

        buttons = GridLayout(cols=4)

        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for text in button_list:
            btn = Button(text=text, font_size=30)
            btn.bind(on_press=self.button_click)
            buttons.add_widget(btn)

        root.add_widget(buttons)

        return root


Calculator().run()
