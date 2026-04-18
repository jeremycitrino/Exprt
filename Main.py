
"""
main.py – Kivy UI with WebView.
Starts the background service and displays the dashboard.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

from kivy_garden.xwebview import WebView

if platform == 'android':
    from android import AndroidService
    from jnius import autoclass


class TradingBotApp(App):
    def build(self):
        self.service = None

        layout = BoxLayout(orientation='vertical')

        self.status_label = Label(text='Bot not running', size_hint=(1, 0.1))
        layout.add_widget(self.status_label)

        btn_start = Button(text='Start Bot', size_hint=(1, 0.1))
        btn_start.bind(on_press=self.start_bot)
        layout.add_widget(btn_start)

        btn_stop = Button(text='Stop Bot', size_hint=(1, 0.1))
        btn_stop.bind(on_press=self.stop_bot)
        layout.add_widget(btn_stop)

        btn_web = Button(text='Reload Dashboard', size_hint=(1, 0.1))
        btn_web.bind(on_press=self.open_dashboard)
        layout.add_widget(btn_web)

        self.webview = WebView(url='http://127.0.0.1:8888', size_hint=(1, 0.7))
        layout.add_widget(self.webview)

        return layout

    def start_bot(self, instance):
        if platform == 'android':
            self._create_notification_channel()
            self.service = AndroidService('TradingBot', 'Bot is running')
            self.service.start('')
            self.status_label.text = 'Bot running (service started)'
            Clock.schedule_once(lambda dt: self.webview.reload(), 5)
        else:
            import subprocess
            subprocess.Popen(['python', 'nostop.py'])
            self.status_label.text = 'Bot running (desktop)'
            Clock.schedule_once(lambda dt: self.webview.reload(), 5)

    def _create_notification_channel(self):
        try:
            Context = autoclass('android.content.Context')
            NotificationManager = autoclass('android.app.NotificationManager')
            NotificationChannel = autoclass('android.app.NotificationChannel')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Build = autoclass('android.os.Build')

            if Build.VERSION.SDK_INT >= 26:
                activity = PythonActivity.mActivity
                manager = activity.getSystemService(Context.NOTIFICATION_SERVICE)
                channel = NotificationChannel(
                    "tradingbot_channel",
                    "Trading Bot Service",
                    NotificationManager.IMPORTANCE_LOW
                )
                manager.createNotificationChannel(channel)
        except Exception as e:
            print(f"Notification channel error: {e}")

    def stop_bot(self, instance):
        if self.service:
            self.service.stop()
            self.status_label.text = 'Bot stopped'
        else:
            self.status_label.text = 'Bot not running'

    def open_dashboard(self, instance):
        self.webview.reload()


if __name__ == '__main__':
    TradingBotApp().run()
