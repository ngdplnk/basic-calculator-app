from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel

__version__ = "0.11"

kv_string = """
AnchorLayout:
    adaptive_height: True
    adaptive_width: True
    anchor_x: 'center'
    anchor_y: 'center'
    padding: [10, 10, 10, 10]
    canvas.before:
        Color:
            rgba: 0.267, 0.267, 0.267, 1  # Background color (#444444)
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        adaptive_height: True
        adaptive_width: True
        orientation: 'vertical'

        MDTextField:
            id: text_field
            hint_text: 'Your expression goes here'
            font_size: '40sp'
            readonly: True
            line_color_normal: 1, 1, 1, 1  # Line color (white)
            anchor_x: 'center'
            anchor_y: 'center'
            adaptive_height: True
            adaptive_width: True
            color: 1, 1, 1, 1  # Text color (white)
        
        GridLayout:
            adaptive_height: True
            adaptive_width: True
            cols: 4
            rows: 6
            padding: [20, 20, 20, 20]
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                text: 'AC'
                padding: [20, 20, 20, 20]
                on_press: app.clear_text_field()

            MDFlatButton:
                text: '('
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: ')'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '%'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '7'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '8'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '9'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '/'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '4'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '5'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '6'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '*'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '1'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '2'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '3'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '-'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '.'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '0'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '←'
                padding: [20, 20, 20, 20]
                on_press: app.backspace()

            MDFlatButton:
                text: '+'
                padding: [20, 20, 20, 20]
                on_press: app.on_button_press(self.text)

            MDFlatButton:
                text: '='
                padding: [20, 20, 20, 20]
                on_press: app.calculate()

        MDLabel:
            text: 'Developed by: @ngdplnk'
            font_size: '10sp'
            color: 1, 1, 1, 1  # Text color (white)
            adaptive_height: True
            adaptive_width: True
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            padding: [20, 20, 20, 20]
"""

class CalculatorApp(MDApp):
    def build(self):
        self.title = 'Basic Calculator Dev'
        self.icon = 'assets/icon.png'
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
        self.expression = self.expression[:-1]
        self.root.ids.text_field.text = self.expression

    def clear_text_field(self):
        self.root.ids.text_field.text = ''
        self.expression = ''

if __name__ == '__main__':
    CalculatorApp().run()
