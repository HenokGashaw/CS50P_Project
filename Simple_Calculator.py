from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class CalculatorApp(App):
    def build(self):
        self.result = Label(text="0", font_size=32, size_hint=(1, 0.2))
        layout = GridLayout(cols=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            '.', '', '', ''
        ]

        for button in buttons:
            btn = Button(text=button, font_size=24)
            btn.bind(on_press=self.on_button_click)
            layout.add_widget(btn)

        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(self.result)
        main_layout.add_widget(layout)

        return main_layout

    def on_button_click(self, instance):
        current_text = self.result.text

        if instance.text == "C":
            self.result.text = '0'
        elif instance.text == "=":
            try:
                self.result.text = str(eval(current_text))
            except Exception:
                self.result.text = "Error"
        else:
            if current_text == '0':
                self.result.text = instance.text
            else:
                if instance.text == '.':
                    if '.' in self.result.text:
                        pass
                    else:
                        self.result.text += instance.text
                else:
                    self.result.text += instance.text

if __name__ == "__main__":
    CalculatorApp().run()


