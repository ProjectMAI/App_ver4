from kivy.app import App
from kivy.lang import Builder

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


kv = Builder.load_file("project.kv")

sm = WindowManager()

screens = [SignUpScreen(name="sign"), RegistrationScreen(name="registration"), MainScreen(name="main"), ProfileScreen(name="profile")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "sign"


class ProjectApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    ProjectApp().run()
