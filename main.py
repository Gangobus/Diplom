# main.py
import sys
import os
import sys
if sys.__stdout__ is None or sys.__stderr__ is None:
   os.environ['KIVY_NO_CONSOLELOG'] = '1'
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from Window import WindowInterface
from kivy.base import EventLoop
from kivymd.uix import label
import ctypes
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hwnd = kernel32.GetConsoleWindow()
if hwnd:
    user32.ShowWindow(hwnd, SW_HIDE)


class MainApp(MDApp):
    #создание окна приложения


    def build(self):
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        self.title = 'BelScribe'
        self.icon = 'icon2.ico'
        Window.size = [1600, 800]
        Builder.load_file(resource_path("Interfase.kv"))

        sm = ScreenManager()
        sm.add_widget(WindowInterface(name="S1T"))

        return sm

    def on_key_down(self, window, key, *args):
        if key == 27:  # Код клавиши "Esc"
            return True  # Предотвращает закрытие приложения
        if key == 282:  # Код клавиши "F1"
            return True  # Предотвращает отображение меню настроек

if __name__ == '__main__':
    EventLoop.window.bind(on_keyboard=MainApp().on_key_down)
    MainApp().run()