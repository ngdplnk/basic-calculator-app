###  Basic Calculator App  ###
### Developed by: @ngdplnk ###

## About the App:
# This is an experimental project to learn about mobile app development using KivyMD.
# Expect bugs and errors, as this is my first attempt at creating a mobile app.
# I want so achieve a clean and simple design, with basic functionality.
# Hope you enjoy it!


## Imports
from kivy.clock import Clock
from kivy import platform
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldHintText,
)
from kivymd.uix.button import (
    MDButton,
    MDButtonText,
)

## Main app class
class BasicCalculator(MDApp):
    # App build and properties
    def build(self):
        self.title = 'Basic Calculator Dev'
        """self.icon = 'assets/icon.png'"""
        self.expression = ''
        return MDScreen(
            MDGridLayout(
                MDTextField(
                    MDTextFieldHintText(
                        text="Your expression goes here",
                    ),
                    id="text_field",
                    text="",
                    mode="outlined",
                    readonly=True,
                    size_hint_x= 0.8,
                ),
                MDGridLayout(
                    MDButton(
                        MDButtonText(
                            text="AC",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        width=60,
                        height=60,
                        on_press=lambda x: self.clear_text_field(),
                    ),
                    MDButton(
                        MDButtonText(
                            text="(",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text=")",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="%",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="7",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="8",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="9",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="/",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="4",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="5",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="6",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="*",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="1",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="2",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="3",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="-",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text=".",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="0",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="DEL",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.backspace(),
                    ),
                    MDButton(
                        MDButtonText(
                            text="+",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        size_hint=(None, None),
                        width=60,
                        height=60,
                        on_press=lambda x: self.on_button_press(x._button_text.text),
                    ),
                    MDButton(
                        MDButtonText(
                            text="=",
                            padding=[20,20,20,20]
                        ),
                        style="tonal",
                        width=60,
                        height=60,
                        on_press=lambda x: self.calculate(),
                    ),
                    cols=4,
                    rows=6,
                    spacing=10,
                    adaptive_size=True,
                    adaptive_height=True,
                    adaptive_width=True,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    padding=[20, 20, 20, 20],
                ),
                cols=1,
                rows=2,
                adaptive_size=True,
                adaptive_height=True,
                adaptive_width=True,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                padding=[20, 20, 20, 20],
            ),
            md_bg_color=self.theme_cls.primaryColor,
        )

    # Button press behavior
    def on_button_press(self, _button_text):
        # Append the button text to the expression and update text field
        self.expression += _button_text
        self.root.get_ids().text_field.text = self.expression

    # Calculate the expression
    def calculate(self):
        try:
            # Evaluate the expression and update text field
            self.root.get_ids().text_field.text = str(eval(self.expression))
        except Exception as e:
            # Handle error cases, such as division by zero
            self.root.get_ids().text_field.text = 'Error'

    # Backspace behavior
    def backspace(self):
        # Remove the last character from the expression and update text field
        self.expression = self.expression[:-1]
        self.root.get_ids().text_field.text = self.expression

    # Clear text field
    def clear_text_field(self):
        # Clear the text field and reset the expression
        self.root.get_ids().text_field.text = ''
        self.expression = ''

    # On start behavior
    def on_start(self):
        self.fps_monitor_start()
        self.theme_cls.dynamic_color = True


## Main function
BasicCalculator().run()

### End of File ###