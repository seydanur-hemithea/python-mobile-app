# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:41:35 2025

@author: Seyda Nur 
"""

import kivy
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from PIL import Image
from pytesseract import pytesseract
from tkinter.filedialog import askopenfile
from kivy.core.window import Window
Window.size=(400,600)

class ExtractingTextApp(MDApp):
    def fileChooser(self,event):
        self.file=askopenfile(mode="r",filetypes=[("png files","*.png")])
        self.image_file=self.file.name
        self.locationLabel.text=self.image_file
        self.locationLabel.pos_hint={"center_x":0.5,"center_y":.2}
        self.extract_text_button.disabled=False
        self.choose_button.disabled=True
    def extract_text(self,event):
        self.path_to_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        path_to_image=self.image_file
        
        ###point TesseRact_cmd to tesseract.exe
        pytesseract.tesseract_cmd=self.path_to_tesseract
        img=Image.open(path_to_image)
        #extract text from ımage
        text=pytesseract.image_to_string(img)
        print(text)
        self.imageText.text=text
    def build(self):
        
        
        self.layout=MDRelativeLayout(md_bg_color=[240/255,100/255,100/255])
        self.imageText=TextInput(text="",pos_hint={"center_x":0.5,"center_y":0.62},
                                 size_hint=(None,None),height=340,width=480,font_size=25,
                                 foreground_color=(0,0.5,0),font_name="Comic")
        self.choose_button=Button(text="Select",pos_hint={"center_x":0.4,"center_y":0.07},
                                  
                                  size_hint=(.2,.1),font_name="Comic",font_size=24,
                                  background_color=(0,1,0),disabled=False,
                                  on_press=self.fileChooser)
        self.extract_text_button=Button(text="Extract",pos_hint={"center_x":.65,"center_y":0.07},
                                  
                                  size_hint=(.2,.1),font_name="Comic",font_size=24,
                                  background_color=(0,1,0),disabled=True,
                                  on_press=self.extract_text)
        self.locationLabel=Label(text="",pos_hint={"center_x":.5,"center_y":0.20},
                                 size_hint=(1,1),font_size=20,color=(0,0,1))
        
        self.layout.add_widget(self.imageText)
        self.layout.add_widget(self.choose_button)
        self.layout.add_widget(self.extract_text_button)
        self.layout.add_widget(self.locationLabel)
        return self.layout
if __name__=="__main__":
       ExtractingTextApp().run()
