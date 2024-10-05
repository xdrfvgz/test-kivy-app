import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        # Erstellen eines BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Erstellen eines TextInput-Feldes
        self.text_input = TextInput(hint_text='Text hier eingeben')

        # Erstellen eines Buttons
        button = Button(text='Klicken Sie mich')
        button.bind(on_press=self.on_button_press)

        # Erstellen eines Labels
        self.label = Label(text='Ergebnis wird hier angezeigt')

        # Hinzufügen der Widgets zum Layout
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.label)

        return layout

    def on_button_press(self, instance):
        # Text vom TextInput-Feld holen und im Label anzeigen
        input_text = self.text_input.text
        self.label.text = f'Eingegebener Text: {input_text}'

if __name__ == '__main__':
    TestApp().run()
