from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", padding=40, spacing=20)

        self.welcome_label = Label(text="", font_size=22)

        logout_button = Button(
            text="Logout",
            size_hint=(1, 0.3)
        )

        logout_button.bind(on_press=self.logout)

        self.layout.add_widget(self.welcome_label)
        self.layout.add_widget(logout_button)

        self.add_widget(self.layout)

    def set_user(self, username, role):
        self.welcome_label.text = f"Welcome {username} ({role})"

    def logout(self, instance):
        self.manager.current = "login"
