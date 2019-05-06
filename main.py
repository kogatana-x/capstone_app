import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.inside = GridLayout()
        self.inside.cols = 2

        field1_text = "First Name:"
        field2_text = "Last Name:"
        field3_text = "Email Address: "
        field4_text = "Phone Number: "

        self.inside.add_widget(Label(text=field1_text))
        self.field1 = TextInput(multiline=False)
        self.inside.add_widget(self.field1)

        self.inside.add_widget(Label(text=field2_text))
        self.field2 = TextInput(multiline=False)
        self.inside.add_widget(self.field2)

        self.inside.add_widget(Label(text=field3_text))
        self.field3 = TextInput(multiline=False)
        self.inside.add_widget(self.field3)

        self.inside.add_widget(Label(text=field4_text))
        self.field4 = TextInput(multiline=False)
        self.inside.add_widget(self.field4)
        self.add_widget(self.inside)

        self.next = Button(text="Next", font_size=40)
        self.next.bind(on_press=self.pressedNext)
        self.add_widget(self.next)

    def pressedNext(self, instance):
        field1 = self.field1.text
        field2 = self.field2.text
        field3 = self.field3.text
        field4 = self.field4.text
        field1_text = "First Name:"
        field2_text = "Last Name:"
        field3_text = "Email Address: "
        field4_text = "Phone Number: "
        
        print(field1_text," ", field1, field2_text," ", field2, field3_text," ", field3, field4_text," ", field4) #return values submitted
        #resetting interactions

        self.field1.text = ""
        self.field2.text = ""
        self.field3.text = ""
        self.field4.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
