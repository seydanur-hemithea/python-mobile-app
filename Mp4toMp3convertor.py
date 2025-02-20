# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:54:23 2025

@author: Seyda Nur
"""
from threading import Thread
from moviepy import VideoFileClip
from tkinter.filedialog import askopenfile

from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp

from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

from kivy.core.window import Window
Window.size=(500,600)
class MyApp(MDApp):

    def fileChooser(self,event):
        self.file=askopenfile(mode="r",filetypes=[("mp4 file","*.mp4")])
        self.mp4_file=self.file.name
        self.mp3_file=self.mp4_file.replace("mp4","mp3")
        
        self.locationLabel.text=self.mp4_file
        self.locationLabel.pos_hint={"center_x":0.5,"center_y":.5}
        
        self.converterButton.pos_hint={"center_x":0.5,"center_y":.35}
    def writeAudio (self):
        self.video=VideoFileClip(self.mp4_file)
        self.audio=self.video.audio
        try:
            self.audio.write_audiofile(self.mp3_file)
            print("completed successfully")
            self.successErrorLabel.text="successfully converted"
            self.successErrorLabel.pos_hint={"center_x":0.5,"center_y":0.2}
            self.audio.close()
            self.video.close()
        except:
            print("Error writing Audio.Please try again")
    def writeAudioThread(self,event):
        
        thread1=Thread(target=self.writeAudio)
        thread1.start()
    
    def build(self):
        layout=MDRelativeLayout(md_bg_color=[240/255,100/255,100/255])
        """self.img=Image(source="indir.png",size_hint=(.5,.5),
                       pos_hint={"center_x":0.5,"center_y":0.85})
        layout.add_widget(self.img)"""
        self.fileChooserLabel=Label(text="Please Select the Mp4 video to Convert",
                                    pos_hint={"center_x":0.4,"center_y":.70},
                                    size_hint=(1,1),font_size=25,color=(0,1,1))
        self.select_button=Button(text="Select",size_hint=(None,None),pos=(520,610),
                                  height=40,on_press=self.fileChooser)
        self.locationLabel=Label(text="",pos_hint={"center_x":0.5,"center_y":20},
                                 size_hint=(1,1),font_size=27,color=(0,0,1))
        
        self.converterButton=Button(text="Convert",pos_hint={"center_x":0.5,"center_y":20},
                                  size_hint=(.2,.1),size=(75,75),font_name="Comic",bold=True,
                                  font_size=24,background_color=(0,1,0),
                                  on_press=self.writeAudioThread)
        
        self.successErrorLabel=Label(text="",pos_hint={"center_x":.5,"center_y":20},
                                     size_hint=(1,1),font_size=25,color=(0,0,1))
        layout.add_widget(self.fileChooserLabel)
        layout.add_widget(self.select_button)
        layout.add_widget(self.locationLabel)
        layout.add_widget(self.converterButton)
        layout.add_widget(self.successErrorLabel)
        return layout
    
if __name__=="__main__":
    MyApp().run()
    