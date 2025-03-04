# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:41:58 2025

@author:Seyda Nur
"""

import cv2
import kivy
import numpy as np
import pyautogui

from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.button import Button


from kivy.clock import Clock
from kivy.core.window import Window

Window.size=(450,150)
class MyApp(MDApp):
    def recordScreen(self,event):
        img=pyautogui.screenshot()
        frame=np.array(img)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.out.write(frame)
    def toggle_recording(self,event):
        if not self.recording:
            self.out=cv2.VideoWriter(self.output_file,self.fourcc,self.fps,self.screen_size)
            self.recording=True
            
            self.record_button.text='Stop Recording'
            Window.minimize()
            Clock.schedule_interval(self.recordScreen,1/30)
        else:
            self.recording=False
            self.record_button.text='Record'
            Clock.unschedule(self.recordScreen)
            self.out.release()
            
    def build(self):
        layout=MDRelativeLayout(md_bg_color=[0,0,0])
        
        self.fourcc=cv2.VideoWriter_fourcc(*'mp4v')
        self.output_file='output.mp4'
        self.fps=30
        self.out=None
        self.recording=False
        self.screen_size=(1920,1080)
        
        
        self.record_button=Button(text="Record",pos_hint={"center_x":0.5,"center_y":0.55},
                                  size_hint=(.8,None),height=100,font_name="Comic",
                                  bold=True,font_size=45,background_color=(1,1,0),
                                  on_press=self.toggle_recording)
       
        layout.add_widget(self.record_button)
        
        return layout
if __name__=="__main__":
    MyApp().run()
