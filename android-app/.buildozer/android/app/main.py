from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton

# KV Language string for the UI layout
kv_string = """
BoxLayout:
    orientation: 'vertical'
    
    MDTextField:
        id: text_field
        hint_text: ''
        font_size: '40sp'
        readonly: True
        padding: [10, 20]
        
    GridLayout:
        cols: 4
        padding: [10, 20]
        
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
        self.title = 'Basic Calculator PRIVATE BUILD 2'
        self.icon = 'icon.png'
        # ICON ATTRIBUTION
        # <a href="https://www.flaticon.es/iconos-gratis/calculadora" title="calculadora iconos">Calculadora iconos creados por Freepik - Flaticon</a>
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
