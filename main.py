from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.dashboard_screen import DashboardScreen
from database import initialize_database


class ITTSApp(App):

    def build(self):
        initialize_database()

        self.sm = ScreenManager()

        self.login_screen = LoginScreen(name="login")
        self.dashboard_screen = DashboardScreen(name="dashboard")

        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.dashboard_screen)

        return self.sm


if __name__ == "__main__":
    ITTSApp().run()

