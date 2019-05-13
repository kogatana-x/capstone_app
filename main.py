# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.graphics import Rectangle


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class ResumeLoaderWindow(Screen):
    def builder(self):
        self.reset()
        sm.current = "builder"
    def update(self):
        if db.validate(self.phoneno.text, self.highed.text):
            MainWindow.current = self.email.text #change this to match -> db takes updated info and slaps it on same line
            self.reset()
            sm.current = "main"
        else:
            invalidInput()


class HomeScreen(Screen):
    def is_done(self):
        sm.current="login"

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""
    Window.clearcolor = (.2,.7,.6,1)

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created




class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',content=Label(text='Invalid username or password.'),size_hint=(None, None), size=(400, 400))
    pop.open()

    self.cols = 2


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

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

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [HomeScreen(name="loading"), LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),ResumeLoaderWindow(name="builder")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "loading"

class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
