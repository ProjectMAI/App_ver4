from kivy.app import App
from kivy.lang import Builder

from kivy.core.window import Window

from kivy.properties import ObjectProperty

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from database import DataBase


Window.size = (360, 640)


class RegistrationScreen(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                
                self.reset()

                sm.current = "sign"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "sign"
    
    def reset(self):
            self.email.text = ""
            self.password.text = ""
            self.namee.text = ""


class SignUpScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def sign(self):
        if db.validate(self.email.text, self.password.text):
            MainScreen.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
    
    def create(self):
        self.reset()
        sm.current = "registration"
    
    def reset(self):
        self.email.text = ""
        self.password.text = ""



class MainScreen(Screen):
    
    def logout(self):
        sm.current = "sign"


class ProfileScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


def invalidForm():
    pop = Popup(title="Invalid Form",
                content=Label(text="Please fill in all inputs with valid information!"),
                size_hint=(None, None), size=(325, 200))

    pop.open()


def invalidLogin():
    pop = Popup(title="Invalid Login",
                content=Label(text="Invalid username or password!"),
                size_hint=(None, None), size=(300, 200))

    pop.open()


kv = Builder.load_file("project.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [SignUpScreen(name="sign"), RegistrationScreen(name="registration"), MainScreen(name="main"), ProfileScreen(name="profile")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "sign"


class ProjectApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    ProjectApp().run()
