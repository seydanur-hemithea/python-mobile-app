# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:40:02 2025
@author: Seyda Nur
"""
import PyPDF3
import pyttsx3
import pdfplumber
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

from kivy.core.window import Window
from threading import Thread
from tkinter.filedialog import askopenfile

Window.size=(500,600)

class MyApp(MDApp):
    def convertToAudio(self):
        self.successErrorLabel.text=""
        try:
            book=open(self.pdf_file,"rb")
            pdfReader=PyPDF3.PdfFileReader(book)
            
            pages=pdfReader.numPages
            finalText=""
            
            try:
                self.successErrorLabel.text="Extracting the Text..."
                self.successErrorLabel.pos_hint={"center_x":0.5,"center_y":.23}
                with pdfplumber.open(self.pdf_file) as pdf:
                    for i in range(0,pages):
                        page=pdf.pages[i]
                        text=page.extract_text()
                        finalText+=text
                self.successErrorLabel.text=""
                self.successErrorLabel.text="Succesfully Extracted the Text"  
                self.successErrorLabel.pos_hint={"center_x":0.5,"center_y":.23}
                try:
                    self.successErrorLabel.text=""
                    self.successErrorLabel.text="Converting... Please Wait"
                    self.successErrorLabel.pos_hint={"center_x":0.5,"center_y":.23}
                
                    engine=pyttsx3.init()
                    engine.save_to_file(finalText,"audioBook.mp3")
                    engine.runAndWait()
                    self.successErrorLabel.text=""
                    
                    self.successErrorLabel.text="Succesfully Converted"
                    self.successErrorLabel.pos_hint={"center_x":0.5,"center_y":.23}
                except:
                    self.successErrorLabel.text="Problem Converting Please Try Again"
                    self.successErrorLabel.pos_hint={"center_x":0.5,"center_y":.23}
            except:
                self.successErrorLabel.text="Problem Extracting the Text"
                self.successErrorLabel.pos_hint={"center_x":0.5,"center_y":.23}
            
        except:
            self.successErrorLabel.text="Problem opening the pdf File "
            self.successErrorLabel.pos_hint={"center_x":0.5,"center_y":.23}
       
        
    
    def convertToAudioThread(self,event):
        
        thread1=Thread(target=self.convertToAudio)
        thread1.start()
    def fileChooser(self,event):
        
        self.file=askopenfile(mode="r",filetypes=[("pdf files","*.pdf")])
        self.pdf_file=self.file.name
        
        
        self.locationLabel.text=self.pdf_file
        self.locationLabel.pos_hint={"center_x":0.5,"center_y":.5}
        
        self.converterButton.pos_hint={"center_x":0.5,"center_y":.35}
    def build(self):
        layout=MDRelativeLayout(md_bg_color=[240/255,100/255,100/255])
        
        self.img=Image(source="indir.png",size_hint=(.5,.7),
                       pos_hint={"center_x":0.5,"center_y":0.85})
        self.fileChooserLabel=Label(text="Please Select the pdf file to Convert",
                                    pos_hint={"center_x":0.4,"center_y":.70},
                                    size_hint=(1,1),font_size=25,color=(0,1,1))
        self.select_button=Button(text="Select",size_hint=(None,None),pos=(500,610),
                                  height=40,on_press=self.fileChooser)
        
        self.locationLabel=Label(text="",pos_hint={"center_x":0.5,"center_y":20},
                                 size_hint=(1,1),font_size=27,color=(0,0,1))
        
        self.converterButton=Button(text="Convert",pos_hint={"center_x":0.5,"center_y":20},
                                  size_hint=(.2,.1),size=(75,75),font_name="Comic",bold=True,
                                  font_size=24,background_color=(0,1,0),
                                  on_press=self.convertToAudioThread)
        
        self.successErrorLabel=Label(text="",pos_hint={"center_x":.5,"center_y":20},
                                     size_hint=(1,1),font_size=25,color=(0,0,1))
        layout.add_widget(self.img)
        layout.add_widget(self.fileChooserLabel)
        layout.add_widget(self.select_button)
        layout.add_widget(self.locationLabel)
        layout.add_widget(self.converterButton)
        layout.add_widget(self.successErrorLabel)
        
        return layout
if __name__=="__main__":
    
    MyApp().run()

