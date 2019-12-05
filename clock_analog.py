#-*-coding: utf-8-*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config
import time
import math

Window.size = (500, 550)
Config.set('graphics', 'resizable', '0')

class MyClock(Widget):
    def __init__(self, **kwargs):
        super(MyClock, self).__init__(**kwargs)
        self.i = 850 #счетчик цикла  и координата х для вывода текста бегущей строки
        self.size_hint = (None, None)
        self.width = 500
        self.height = 550
        Clock.schedule_interval(self.clock_time_func, 0.1)

    def clock_time_func(self, instance):
        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos = (0, 0), size = (500, 550))#фон приложения

            Color(0.09, 0.29, 0.37, 0.8)
            Ellipse(pos = (5, 5), size = (490, 490)) #фон циферблата

            Color(0, 0.3, 1)
            Line(ellipse=(50, 50, 400, 400), width = 1.2) #циферблат  просто круг
            Point(points = (250, 250), pointsize = 2)#выводим точку - центр циферблата

            i = 0
            while i < 60: #цикл вывода секундных рисочек
                i = i + 1
                Line(points = (250 + 210 * math.cos(-i * 6 * math.pi / 180 + math.pi / 2),
                               250 - 210 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                               250 + 190 * math.cos(-6 * i * math.pi / 180 + math.pi / 2),
                               250 - 190 * math.sin(-6 * i * math.pi / 180 + math.pi / 2)), width = 1)
                if i % 5 == 0: #когда i кратно 5 выводим более жирную рисочку для обозначения часов
                    Line(points = (250 + 215 * math.cos(-i * 6 * math.pi / 180 + math.pi / 2),
                                   250 - 215 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                                   250 + 190 * math.cos(-6 * i * math.pi / 180 + math.pi / 2),
                                   250 - 190 * math.sin(-6 * i * math.pi / 180 + math.pi / 2)), width = 2.4)

            i = 0
            while i < 12: #цикл вывода цифр часов
                i += 1
                self.add_widget(Label(text=str(i), pos_hint=(None, None), size_hint=(None, None),
                       width=30, height=30, color=(0.82, 0.23, 0.47, 0.8), font_size=18,
                       pos=(235 + 230 * math.cos(30 * (-i) * math.pi / 180 + math.pi / 2),
                            235 + 230 * math.sin(i * 30 * math.pi / 180 + math.pi / 2))))

            time_now = time.localtime() #получаем текущее время
            time_sec = int(time.strftime('%S', time_now)) #получаем секунды из переменной time_now
            time_hour = int(time.strftime('%I', time_now)) #получаем часы из переменной time_now
            time_min = int(time.strftime('%M', time_now)) #получаем минуты из переменной time_now
            sec_angle = 6 * time_sec                      #угол отклонения секундной стрелки за 1 секунду
            min_angle = time_min * 6 + time_sec * 0.1    #угол отклонения минутной стрелки за 1 секунду
            hour_angle = time_hour * 30 + time_min * 60 * (30 / 3600) #угол отклонения часовой стрелки за 1 секунду
            Color(0, 0.3, 1)
            # рисуем минутную стрелку
            Line(points=(250, 250,
                         250 + 180 * math.cos(-min_angle * math.pi / 180 + math.pi / 2),
                         250 + 180 * math.sin(min_angle * math.pi / 180 + math.pi / 2)), width=2)
            # рисуем часовую стрелку
            Line(points=(250, 250,
                         250 + 150 * math.cos(-hour_angle * math.pi / 180 + math.pi / 2),
                         250 + 150 * math.sin(hour_angle * math.pi / 180 + math.pi / 2)), width=3)
            # рисуем секундную стрелку
            Color(0.5, 0.3, 0.2)
            Line(points=(250, 250,
                         250 + 180 * math.cos(-sec_angle * math.pi / 180 + math.pi / 2),
                         250 + 180 * math.sin(sec_angle * math.pi / 180 + math.pi / 2)), width=1.2)
            # Задаем бегущую строку
            text_bottom = Label(text='Бегущая строка вверху над часами',
                                pos_hint=(None, None), size_hint=(None, None),
                                width=100, height=30, color=(1, 0.3, 0.2, 1), font_size=18,
                                pos=(self.i, 525))
            self.add_widget(text_bottom)
            self.i = self.i - 10
            if self.i <= -460:
                self.i = 850

            self.remove_widget(text_bottom)

class MyClockApp(App):
    def build(self):
        return MyClock()

if __name__ == '__main__':
    MyClockApp().run()

