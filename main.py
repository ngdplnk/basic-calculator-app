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
        hint_text: '0'
        font_size: '40sp'
        readonly: True
        padding: [10, 20]
        
    GridLayout:
        cols: 4
        padding: [10, 20]
        
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
            text: '='
            on_press: app.on_button_press(self.text)
        
        MDFlatButton:
            text: '+'
            on_press: app.on_button_press(self.text)
"""

class CalculatorApp(MDApp):
    def build(self):
        self.expression = ''
        return Builder.load_string(kv_string)

    def on_button_press(self, button_text):
        if button_text == '=':
            try:
                # Evaluate the expression and update text field
                self.root.ids.text_field.text = str(eval(self.expression))
            except Exception as e:
                # Handle error cases, such as division by zero
                self.root.ids.text_field.text = 'Error'
            finally:
                # Reset expression
                self.expression = ''
        else:
            # Update expression with button text
            self.expression += button_text
            self.root.ids.text_field.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
