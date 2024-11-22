from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        self.label = Label(text="Натисніть кнопку")
        button = Button(text="Натискати")


        button.bind(on_press=self.change_text)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def change_text(self, instance):
        self.label.text = "Кнопка натиснута!"


if __name__ == "__main__":
    MyApp().run()