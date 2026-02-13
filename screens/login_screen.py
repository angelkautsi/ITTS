from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        self.username_input = TextInput(
            hint_text="Username",
            multiline=False
        )

        self.password_input = TextInput(
            hint_text="Password",
            password=True,
            multiline=False
        )

        login_button = Button(
            text="Login",
            size_hint=(1, 0.5)
        )

        login_button.bind(on_press=self.validate_login)

        self.message = Label(text="")

        layout.add_widget(Label(text="ITTS Login", font_size=24))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        layout.add_widget(self.message)

        self.add_widget(layout)

    def validate_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        conn = sqlite3.connect("itts.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            username = user[1]
            role = user[3]

            dashboard = self.manager.get_screen("dashboard")
            dashboard.set_user(username, role)

            self.manager.current = "dashboard"
        else:
            self.message.text = "Invalid username or password."

