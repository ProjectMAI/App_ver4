from kivy.app import App

from kivy.core.window import Window

from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


Window.size = (360, 640)

class RegistrationScreen(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)


class SignUpScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class ProjectApp(App):
    pass

if __name__ == "__main__":
    ProjectApp().run()