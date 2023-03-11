
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random
import string
import json
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
import time
import threading
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.scrollview import ScrollView




class MyTextInput(TextInput):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.text = text



class MyTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.default_tab_text = 'Привет'
        scroll_view_1 = ScrollView()
        layout_1 = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        layout_1.bind(minimum_height=layout_1.setter('height'))
        #layout_1.add_widget(Label(text="Привет друг\n"*10))
        layout_1.add_widget(TextInput(text="Привет друг\n"*4, halign='center', size_hint_y=None, background_color=(0,0,0,0), foreground_color=(1,1,1,1), readonly=True))
        scroll_view_1.add_widget(layout_1)
        self.default_tab_content = scroll_view_1
        

        #self.default_tab_content = BoxLayout(orientation='vertical')
        #self.default_tab_content.add_widget(BoxLayout())
        
        
        # создаем вторую вкладку
        second_tab = TabbedPanelItem(text='Настройки')
        scroll_view_2 = ScrollView()
        layout_2 = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        layout_2.bind(minimum_height=layout_2.setter('height'))        
        layout_2.add_widget(MainWidget(size_hint_y=None, height=700))
        scroll_view_2.add_widget(layout_2)
        second_tab.content = scroll_view_2
        self.add_widget(second_tab)
class MainWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.left_col = BoxLayout(orientation='vertical', size_hint_x=0.7, size_hint_y=None)
        self.right_col = BoxLayout(orientation='vertical', size_hint_x=0.3, size_hint_y=None)
        self.flag = True # добавляем атрибут flag и устанавливаем его в True
        try:
            with open('vari.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:    
            data = {}
            
        K = ['1', '2', '3', '4', '5', '6', '7']
            
        # Создание полей ввода
        fields = ['1111111111111111111111111111111111111111111', '2222222222222222222222222222222222222222222222222222222222', '3333333333333333333333333333333333333333333333333333333333333333', '444444444444444444444444444444', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'ПППППППППППППППППППППППППППП', 'ВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВ', 'ККККККККККККККККККККККККККККККККККККККККККККККККККККККККККК', 'ЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ', 'РРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР']
        
        for field in fields:
            if field == '1111111111111111111111111111111111111111111' or field == '2222222222222222222222222222222222222222222222222222222222':
                self.left_col.add_widget(TextInput(text=field,  size_hint_y=None, height=50, background_color=(0,0,0,0), foreground_color=(1,1,1,1), readonly=True))
                self.right_col.add_widget(TextInput(text=data.get(field, ''), password=True, size_hint_y=None, height=50))
            else:    
                self.left_col.add_widget(TextInput(text=field,  size_hint_y=None, height=50, background_color=(0,0,0,0), foreground_color=(1,1,1,1), readonly=True))
                self.right_col.add_widget(TextInput(text=data.get(field, ''), input_filter='int', size_hint_y=None, height=50))

        # Создание выпадающих списков
        
        self.left_col.add_widget(TextInput(text="1221",  size_hint_y=None, height=50, background_color=(0,0,0,0), foreground_color=(1,1,1,1), readonly=True))
        self.right_col.add_widget(Spinner(text=data.get('12', ''), values=('12', '21'), size_hint_y=None, height=50))

        self.left_col.add_widget(TextInput(text="45646",  size_hint_y=None, height=50, background_color=(0,0,0,0), foreground_color=(1,1,1,1), readonly=True))
        self.right_col.add_widget(Spinner(text=data.get('111', ''), values=K, size_hint_y=None, height=50))

        self.left_col.add_widget(TextInput(text="45646",  size_hint_y=None, height=50, background_color=(0,0,0,0), foreground_color=(1,1,1,1), readonly=True))
        self.right_col.add_widget(Spinner(text=data.get('1111', ''), values=('1111', '2222'), size_hint_y=None, height=50))
        
        # Создание кнопок
        save_button = Button(text='Сохранить', size_hint_y=None, height=50)
        save_button.bind(height=save_button.setter('height'))
        save_button.bind(on_press=self.save_data)
        self.right_col.add_widget(save_button)

        run_button = Button(text='Пуск', size_hint_y=None, height=50)
        run_button.bind(height=run_button.setter('height'))
        run_button.bind(on_press=self.run_script)

        stop_button = Button(text='Стоп', size_hint_y=None, height=50)
        stop_button.bind(height=stop_button.setter('height'))
        stop_button.bind(on_press=self.stop_script)
        
        bottom_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        bottom_row.add_widget(run_button)
        bottom_row.add_widget(stop_button)
        
        self.left_col.add_widget(bottom_row)

        self.add_widget(self.left_col)
        self.add_widget(self.right_col)

    def reset_colors(self):
        for child in self.right_col.children:
            if isinstance(child, TextInput):
                child.background_color = [1, 1, 1, 1]


    def save_data(self, instance):
        data = {}
        for i, child in enumerate(self.right_col.children):
            if isinstance(self.left_col.children[i], Label):
                name = self.left_col.children[i].text
                if isinstance(child, TextInput):
                    data[name] = child.text
                    if child.text == '':
                        child.background_color = [1, 0, 0, 1]
                    else:
                        child.background_color = [1, 1, 1, 1]
                elif isinstance(child, Spinner):
                    data[name] = child.text
        with open('vari.json', 'w') as f:
            json.dump(data, f)
    

    def run_script(self, instance):
        with open('vari.json', 'r') as f:
            data = json.load(f)
        print(data)

        # запуск потока, который выполнит код в цикле while в фоновом режиме
        self.flag = True
        t = threading.Thread(target=self.run_loop)
        t.start()

    def stop_script(self, instance):
        self.flag = False

    def run_loop(self):
        while self.flag:
            print(1111111111)
            time.sleep(5)

    def on_stop(self):
        self.stop()
        print("App is closing")
        
class TabbedPanelApp(App):
    def build(self):
        
        return MyTabbedPanel()


if __name__ == '__main__':
    TabbedPanelApp().run()
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 18:11:55 2023

@author: Sergey
"""

