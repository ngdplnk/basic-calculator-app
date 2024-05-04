from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel

__version__ = "0.7-alpha"

kv_string = """
AnchorLayout:
    adaptive_height: True
    adaptive_width: True
    anchor_x: 'center'
    anchor_y: 'center'
    canvas.before:
        Color:
            rgba: 0.267, 0.267, 0.267, 1  # Background color (#444444)
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size_hint: 0.5, 0.5  # Set the size of the widget to 50 percent of its parent's size
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Set the position of the widget to the center of its parent
        adaptive_height: True
        adaptive_width: True

        MDTextField:
            id: text_field
            hint_text: 'Your expression goes here'
            font_size: '40sp'
            readonly: True
            padding: [10, 20]
            color: 1, 1, 1, 1  # Text color (white)
        
        GridLayout:
            cols: 4
            size_hint: 1, 1  # Set the size of the widget to 100 percent of its parent's size
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Set the position of the widget to the center of its parent
            padding: [10, 20]
            adaptive_height: True
            adaptive_width: True
            anchor_x: 'center'
            anchor_y: 'center'

            MDFlatButton:
                text: 'AC'
                on_press: app.clear_text_field()

            MDFlatButton:
                text: '('
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: ')'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '%'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '7'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '8'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '9'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '/'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '4'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '5'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '6'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '*'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '1'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '2'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '3'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '-'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '.'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '0'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '<-'
                on_press: app.backspace()

            MDFlatButton:
                text: '+'
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '='
                on_press: app.calculate()
"""

class CalculatorApp(MDApp):
    def build(self):
        self.title = 'Basic Calculator'
        self.icon = 'icon.png'
        # ICON ATTRIBUTION
        # <a href="https://www.flaticon.es/iconos-gratis/calculadora" title="calculadora iconos">Calculadora iconos creados por Freepik - Flaticon</a>
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.expression = ''
        return Builder.load_string(kv_string)

    def on_button_press(self, button_text):
        self.expression += button_text
        self.root.ids.text_field.text = self.expression

    def calculate(self):
        try:
            # Evaluate the expression and update text field
            self.root.ids.text_field.text = str(eval(self.expression))
        except Exception as e:
            # Handle error cases, such as division by zero
            self.root.ids.text_field.text = 'Error'

    def backspace(self):
        # Remove the last character from the expression
        self.expression = self.expression[:-1]
        self.root.ids.text_field.text = self.expression

    def clear_text_field(self):
        self.root.ids.text_field.text = ''
        self.expression = ''

if __name__ == '__main__':
    CalculatorApp().run()
