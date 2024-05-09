from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

__version__ = "0.9"

kv_string = """
AnchorLayout:
    canvas.before:
        Color:
            rgba: 68/255, 68/255, 68/255, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 0.85, 0.85
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        adaptive_height: True
        adaptive_width: True
        canvas.before:
            Color:
                rgba: 68/255, 68/255, 68/255, 1
            Rectangle:
                size: self.size
                pos: self.pos

        MDLabel:
            id: title
            text: 'Basic Calculator Alpha'
            halign: 'center'
            size_hint_y: None
            height: 50
                
        MDTextField:
            id: text_field
            hint_text: 'Enter expression'
            font_size: '30sp'
            readonly: True
            padding: [10, 20]
        
        GridLayout:
            cols: 4
            spacing: 5
            padding: 10
            adaptive_height: True
            adaptive_width: True
            halign: 'center'

            MDButton:
                id: ac_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.clear_text_field()
                MDButtonText:
                    text: 'AC'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: parentheses_open_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('(')
                MDButtonText:
                    text: '('
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: parentheses_close_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press(')')
                MDButtonText:
                    text: ')'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: percentage_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('%')
                MDButtonText:
                    text: '%'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: seven_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('7')
                MDButtonText:
                    text: '7'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: eight_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('8')
                MDButtonText:
                    text: '8'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: nine_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('9')
                MDButtonText:
                    text: '9'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: division_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('/')
                MDButtonText:
                    text: '/'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: four_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('4')
                MDButtonText:
                    text: '4'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: five_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('5')
                MDButtonText:
                    text: '5'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: six_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('6')
                MDButtonText:
                    text: '6'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: multiplication_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('*')
                MDButtonText:
                    text: 'x'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: one_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('1')
                MDButtonText:
                    text: '1'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: two_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('2')
                MDButtonText:
                    text: '2'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: three_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('3')
                MDButtonText:
                    text: '3'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: subtraction_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('-')
                MDButtonText:
                    text: '-'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: dot_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('.')
                MDButtonText:
                    text: '.'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: zero_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('0')
                MDButtonText:
                    text: '0'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: backspace_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.backspace()
                MDButtonText:
                    text: '⌫'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: addition_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.on_button_press('+')
                MDButtonText:
                    text: '+'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

            MDButton:
                id: equal_button
                size_hint: None, None
                adaptive_height: True
                adaptive_width: True
                on_press: app.calculate()
                MDButtonText:
                    text: '='
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'

"""

class CalculatorApp(MDApp):
    def build(self):
        self.title = 'Basic Calculator Alpha'
        self.icon = 'icon.png'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.expression = ''
        return Builder.load_string(kv_string)

    def on_button_press(self, button_text):
        self.expression += button_text
        self.root.ids.text_field.text = self.expression

    def calculate(self):
        try:
            self.root.ids.text_field.text = str(eval(self.expression))
            self.expression = self.root.ids.text_field.text
        except Exception as e:
            self.root.ids.text_field.text = 'Error'

    def backspace(self):
        self.expression = self.expression[:-1]
        self.root.ids.text_field.text = self.expression

    def clear_text_field(self):
        self.root.ids.text_field.text = ''
        self.expression = ''

if __name__ == '__main__':
    CalculatorApp().run()
