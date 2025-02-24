# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:39:44 2025

@author: Seyda Nur

"""
import os
import random
import kivy
import time

from kivy.app import App
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar

Window.size=(400,600)
class MyApp(MDApp):
    def build(self):
        layout=MDRelativeLayout(md_bg_color=[0,0,0.5,1])
        
        self.music_dir="C:/"
        self.music_files=os.listdir(self.music_dir)
        print( self.music_files)
        self.song_list=[x for x in  self.music_files if x.endswith("mp3")]
        print(self.song_list)
        self.song_count=len(self.song_list)
        print(self.song_count)
        
        self.songLabel=Label(pos_hint={"center_x":0.4,"center_y":0.96},size_hint=(1,1),font_size=18)
        self.albumImage=Image(pos_hint={"center_x":0.5,"center_y":0.55},size_hint=(.8,.75))
        self.progressbar=ProgressBar(max=100,value=0,pos_hint={"center_x":0.5,"center_y":0.12},
                                                               size_hint=(.8,.75))
        self.play_button=MDIconButton(pos_hint={"center_x":0.4,"center_y":0.05},
                                      icon="play.png",
                                      on_press=self.playaudio)
                                    
         
        self.stop_button=MDIconButton(pos_hint={"center_x":0.55,"center_y":0.05},
                                      icon="stop.png",on_press=self.stopaudio,disabled=True)
        
        
        self.volumeslider=Slider(min=0,max=1,value=0.5,orientation="horizontal",
                                 pos_hint={"center_x":0.2,"center_y":0.05},size=(.02,.02),
                                 size_hint=(.3,.10))
        self.currenttime=Label(text="00:00",pos_hint={"center_x":0.16,"center_y":0.145},
                                size_hint=(1,1),font_size=18)
        
        self.totaltime=Label(text="00:00",pos_hint={"center_x":0.84,"center_y":0.145},
                                size_hint=(1,1),font_size=18)
         
         
                     
        layout.add_widget(self.play_button)
        layout.add_widget(self.stop_button)
        layout.add_widget(self.songLabel)
        layout.add_widget(self.albumImage)
        layout.add_widget(self.progressbar)
        layout.add_widget(self.currenttime)
        layout.add_widget(self.totaltime)
        layout.add_widget(self.volumeslider)
       
        def volume(instance,value):
            self.sound.volume=value
            
        self.volumeslider.bind(value=volume)
        
        return layout
        Clock.schedule_once(self.playaudio)
    
       
    def playaudio(self,obj):
        self.play_button.disabled=True
        self.stop_button.disabled=False
        self.song_title=self.song_list[random.randrange(0,self.song_count)]
        print(self.song_title)
        self.sound=SoundLoader.load('{}/{}'.format(self.music_dir,self.song_title))
        self.songLabel.text="===Playing=="+self.song_title[0:-4]
        self.albumImage.source=self.song_title[0]+".jpg"
        self.progressbarEvent=Clock.schedule_interval(self.updateprogressbar,self.sound.length/60)
        self.timeEvent=Clock.schedule_interval(self.settime,1)

        self.sound.play()
    def stopaudio(self,obj):
        self.stop_button.disabled=True
        self.play_button.disabled=False
        self.sound.stop()
        self.progressbarEvent.cancel()
        
        self.timeEvent.cancel()
        self.progressbar.value=0
        self.currenttime.text="00:00"
        self.totaltime.text="00:00"
    def updateprogressbar(self,value):
        if self.progressbar.value<100:
            self.progressbar.value+=1
    def settime(self,t):
        current_time=time.strftime('%M:%S',time.gmtime(self.progressbar.value))
        total_time=time.strftime('%M:%S',time.gmtime(self.sound.length))
        
        self.currenttime.text=current_time
        self.totaltime.text=total_time
                                 
    
if __name__=="__main__":
    MyApp().run()

